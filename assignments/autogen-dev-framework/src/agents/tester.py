from autogen.agentchat import AssistantAgent
from typing import Dict, List, Optional, Any
import logging
from pathlib import Path
from src.config import Config
from src.monitor import measure_time

logger = logging.getLogger(__name__)

class TestingAgent(AssistantAgent):
    """
    Agent specialized in writing and executing test cases for code validation.
    Inherits from AutoGen's AssistantAgent for native integration.
    """
    
    def __init__(
        self,
        name: str = "tester",
        llm_config: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize the testing agent with AutoGen's native configuration.

        Args:
            name: Agent identifier
            llm_config: Language model configuration
            **kwargs: Additional configuration options
        """
        system_message = """
        You are responsible for comprehensive testing of code.
        
        Responsibilities:
        1. Write unit tests
        2. Perform integration testing
        3. Validate edge cases
        4. Ensure code coverage
        
        Guidelines:
        - Follow testing best practices
        - Write clear test cases
        - Include positive and negative tests
        - Document test scenarios
        
        Use TERMINATE when testing is complete.
        """
        
        llm_config = llm_config or Config.get_agent_config("tester")
        
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
    async def generate_test_suite(
        self,
        code: str,
        requirements: Dict[str, Any],
        framework: str = "pytest"
    ) -> Dict[str, Any]:
        """
        Generates a comprehensive test suite for the provided code.
        
        Args:
            code: Source code to test
            requirements: Testing requirements and constraints
            framework: Testing framework to use
            
        Returns:
            Dict containing test suite and metadata
        """
        try:
            messages = [{
                "role": "user",
                "content": f"""
                Generate a complete test suite for:
                
                Code:
                ```python
                {code}
                ```
                
                Requirements:
                {requirements}
                
                Use {framework} framework.
                Include:
                1. Unit tests
                2. Edge cases
                3. Error scenarios
                4. Documentation
                """
            }]
            
            response = await self.generate_reply(messages)
            
            # Save test suite to file
            test_file = self.work_dir / f"test_{Path(requirements.get('filename', 'code')).stem}.py"
            with open(test_file, 'w') as f:
                f.write(response)
            
            return {
                'success': True,
                'test_suite': response,
                'test_file': str(test_file),
                'framework': framework
            }
            
        except Exception as e:
            logger.error(f"Error generating test suite: {str(e)}", exc_info=True)
            return {
                'success': False,
                'error': str(e)
            }

    @measure_time
    async def validate_implementation(
        self,
        code: str,
        tests: str,
        requirements: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Validates code implementation against test suite and requirements.
        
        Args:
            code: Implementation to validate
            tests: Test suite to run
            requirements: Validation requirements
            
        Returns:
            Dict containing validation results
        """
        try:
            messages = [{
                "role": "user",
                "content": f"""
                Validate implementation against tests:
                
                Code:
                ```python
                {code}
                ```
                
                Tests:
                ```python
                {tests}
                ```
                
                Requirements:
                {requirements}
                
                Provide:
                1. Test coverage analysis
                2. Requirements compliance
                3. Edge case handling
                4. Performance considerations
                """
            }]
            
            response = await self.generate_reply(messages)
            
            return {
                'success': True,
                'validation': response,
                'passed': 'TERMINATE' in response
            }
            
        except Exception as e:
            logger.error(f"Error in validation: {str(e)}", exc_info=True)
            return {
                'success': False,
                'error': str(e)
            }
