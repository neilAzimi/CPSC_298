import asyncio
from autogen.agentchat import AssistantAgent
from typing import Dict, List, Optional, Any
import logging
import subprocess
from pathlib import Path
from src.config import Config
from src.monitor import measure_time

logger = logging.getLogger(__name__)

class ExecutorAgent(AssistantAgent):
    """An agent specialized in executing and testing code."""
    
    def __init__(
        self,
        name: str = "executor",
        llm_config: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize the executor agent.
        
        Args:
            name: Agent identifier
            llm_config: Language model configuration
            **kwargs: Additional configuration options
        """
        system_message = """
        You are an expert code execution agent that safely runs and tests code.
        
        Your responsibilities:
        1. Execute code safely
        2. Capture and report outputs
        3. Handle execution errors
        4. Provide execution feedback
        
        Use TERMINATE when execution is complete or if there are critical errors.
        """
        
        llm_config = llm_config or Config.get_agent_config("executor")
        
        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config,
            **kwargs
        )
        
        # Set up work directory
        self.work_dir = Path(Config.WORK_DIR)
        self.work_dir.mkdir(parents=True, exist_ok=True)

    @measure_time
    async def execute_code(
        self,
        code: str,
        filename: str,
        timeout: int = 30
    ) -> Dict[str, Any]:
        """
        Execute Python code and capture the output.
        
        Args:
            code: The code to execute
            filename: The name of the file to save the code in
            timeout: Maximum execution time in seconds
            
        Returns:
            Dict containing execution results
        """
        try:
            # Save code to file
            file_path = self.work_dir / filename
            with open(file_path, 'w') as f:
                f.write(code)
            
            # Execute the code
            result = subprocess.run(
                ['python', str(file_path)],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr if result.returncode != 0 else None,
                'file_path': str(file_path)
            }
            
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': f'Execution timed out after {timeout} seconds'
            }
        except Exception as e:
            logger.error(f"Error executing code: {str(e)}", exc_info=True)
            return {
                'success': False,
                'error': str(e)
            }

    @measure_time
    async def validate_execution(
        self,
        execution_result: Dict[str, Any],
        expected_output: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Validate the execution results.
        
        Args:
            execution_result: Results from code execution
            expected_output: Optional expected output to validate against
            
        Returns:
            Dict containing validation results
        """
        try:
            messages = [{
                "role": "user",
                "content": f"""
                Validate the following code execution results:
                
                Execution Output:
                {execution_result.get('output', 'No output')}
                
                Error Output:
                {execution_result.get('error', 'No errors')}
                
                Expected Output:
                {expected_output or 'Not specified'}
                
                Provide:
                1. Validation status
                2. Output analysis
                3. Recommendations
                """
            }]
            
            response = await self.generate_reply(messages)
            
            validation_passed = (
                execution_result['success'] and
                (not expected_output or expected_output in execution_result.get('output', ''))
            )
            
            return {
                'success': validation_passed,
                'analysis': response,
                'matches_expected': validation_passed if expected_output else None
            }
            
        except Exception as e:
            logger.error(f"Error in validation: {str(e)}", exc_info=True)
            return {
                'success': False,
                'error': str(e)
            }
