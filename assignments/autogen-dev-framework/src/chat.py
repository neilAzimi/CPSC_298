import asyncio
from autogen.agentchat import AssistantAgent, GroupChat, GroupChatManager, UserProxyAgent
from typing import Optional, Dict, List, Any, Union, Callable
from dataclasses import dataclass
import logging
from src.config import Config
from src.monitor import measure_time, PerformanceMonitor

# Update imports for specialized agents
from src.agents.planner import PlanningAgent
from src.agents.coder import CoderAgent
from src.agents.debugger import DebuggingAgent
from src.agents.executor import ExecutorAgent
from src.agents.tester import TestingAgent

logging.basicConfig(**Config.get_logging_config())
logger = logging.getLogger(__name__)

@dataclass
class TaskResult:
    success: bool
    output: Any
    message: str
    next_steps: Optional[List[str]] = None

class DevelopmentChat:
    def __init__(self, max_rounds: int = 50):
        """
        Initialize the development chat system.
        
        Args:
            max_rounds: Maximum number of conversation rounds
        """
        self.monitor = PerformanceMonitor()
        self.max_rounds = max_rounds
        self._initialize_agents()
        self._setup_group_chat()
    
    def _initialize_agents(self):
        """Initialize all agents with proper roles and configurations"""
        # Initialize user proxy first
        self.user_proxy = UserProxyAgent(
            name="user_proxy",
            system_message="""You are the user's proxy, responsible for:
            1. Initiating development tasks
            2. Providing requirements and context
            3. Validating final results
            4. Managing code execution
            Use TERMINATE when the task is completed successfully.""",
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,
                "timeout": 60,
            },
            human_input_mode="TERMINATE"
        )
        
        # Initialize planner
        self.planner = PlanningAgent()
        
        # Initialize specialized agents
        self.agent_pool = {
            'coder': CoderAgent(),
            'executor': ExecutorAgent(),
            'debugger': DebuggingAgent(),
            'tester': TestingAgent()
        }
        
        # Store the preferred order for state transitions
        self.agent_order = [
            self.user_proxy,
            self.planner,
            self.agent_pool['coder'],
            self.agent_pool['executor'],
            self.agent_pool['tester'],
            self.agent_pool['debugger']
        ]
    
    def _get_next_speaker(self, last_speaker: AssistantAgent) -> Optional[AssistantAgent]:
        """
        Determine the next speaker based on workflow state.
        
        Args:
            last_speaker: The agent who spoke last
            
        Returns:
            The next agent to speak or None to terminate
        """
        try:
            current_index = self.agent_order.index(last_speaker)
            next_index = current_index + 1
            
            # Check if we've reached the end of the workflow
            if next_index >= len(self.agent_order):
                return None
                
            return self.agent_order[next_index]
            
        except ValueError:
            # If speaker not found in order, default to planner
            return self.planner
    
    def _setup_group_chat(self):
        """Setup GroupChat with enhanced configuration"""
        # Collect all agents in proper order
        all_agents = self.agent_order
        
        # Configure the group chat
        self.group_chat = GroupChat(
            agents=all_agents,
            messages=[],
            max_round=self.max_rounds,
            speaker_selection_method="round_robin",  # Use round robin for predictable flow
            allow_repeat_speaker=False  # Prevent agent from speaking twice in a row
        )
        
        # Configure the manager with retry and timeout settings
        self.chat_manager = GroupChatManager(
            groupchat=self.group_chat,
            llm_config={
                **Config.get_agent_config("planner"),
                "timeout": 600,  # 10 minute timeout
                "retry_on_timeout": True,
                "max_retries": 3,
                "seed": 42  # For reproducibility
            }
        )
    
    async def _handle_conversation_error(
        self,
        error: Exception,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Handle conversation errors with recovery attempts.
        
        Args:
            error: The exception that occurred
            context: Current conversation context
            
        Returns:
            Dict containing error handling results
        """
        logger.error(f"Conversation error: {str(error)}", exc_info=True)
        
        try:
            # Create error analysis message
            error_message = {
                "role": "user",
                "content": f"""
                Error occurred: {str(error)}
                
                Context:
                {context}
                
                Please analyze and suggest recovery steps.
                """
            }
            
            # Get analysis from debugger
            response = await self.agent_pool['debugger'].generate_reply([error_message])
            
            return {
                'status': 'recovered' if 'TERMINATE' in response else 'failed',
                'error': str(error),
                'recovery_steps': response,
                'debug_output': response
            }
            
        except Exception as recovery_error:
            logger.error("Recovery attempt failed", exc_info=True)
            return {
                'status': 'failed',
                'error': str(error),
                'recovery_error': str(recovery_error)
            }

    async def _plan_and_execute(self, task: str) -> Dict[str, Any]:
        """Execute task with enhanced error handling and state management"""
        try:
            # Start conversation with proper context
            initial_context = {
                'task': task,
                'timestamp': self.monitor.get_timestamp(),
                'session_id': id(self)
            }
            
            # Initiate the chat with the user proxy
            await self.user_proxy.initiate_chat(
                self.planner,
                message=task
            )
            
            # Check termination and success conditions
            is_terminated = any(
                "TERMINATE" in str(msg.get("content", ""))
                for msg in self.group_chat.messages[-3:]
            )
            
            # Collect performance metrics
            metrics = {
                **self.monitor.get_metrics(),
                'rounds_completed': len(self.group_chat.messages),
                'agents_involved': [msg.get('sender') for msg in self.group_chat.messages]
            }
            
            # Get the last message as the result
            last_message = self.group_chat.messages[-1] if self.group_chat.messages else None
            result = last_message.get('content') if last_message else None
            
            return {
                'status': 'completed' if is_terminated else 'ongoing',
                'results': result,
                'history': self.group_chat.messages,
                'metrics': metrics
            }
            
        except Exception as e:
            return await self._handle_conversation_error(e, {'task': task})

    async def chat_loop(self):
        """Enhanced chat loop with better state management"""
        try:
            while True:
                # Get user input
                user_input = input("\nEnter your task (or 'exit' to quit): ")
                if user_input.lower() == 'exit':
                    break
                
                # Reset conversation state for new task
                self.group_chat.messages = []
                
                # Execute task
                result = await self._plan_and_execute(user_input)
                
                # Display results based on status
                if result['status'] == 'completed':
                    print("\n✅ Task completed successfully!")
                    print(f"Results: {result['results']}")
                elif result['status'] == 'recovered':
                    print("\n⚠️ Task completed with recovery steps")
                    print(f"Recovery steps: {result.get('recovery_steps', [])}")
                elif result['status'] == 'failed':
                    print(f"\n❌ Task failed: {result.get('error')}")
                else:
                    print("\n⏳ Task is ongoing...")
                
                # Display metrics in debug mode
                if Config.DEBUG_MODE:
                    print("\nMetrics:", result.get('metrics', {}))
                    print(f"Conversation rounds: {len(self.group_chat.messages)}")
        
        except KeyboardInterrupt:
            print("\n\nChat session terminated by user.")
        except Exception as e:
            logger.error("Chat loop error", exc_info=True)
            print(f"\nError in chat loop: {str(e)}")
            if Config.DEBUG_MODE:
                raise

def main():
    """Entry point for the chat application"""
    chat = DevelopmentChat(max_rounds=50)
    asyncio.run(chat.chat_loop())

if __name__ == "__main__":
    main()