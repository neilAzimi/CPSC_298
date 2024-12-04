import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from pathlib import Path
import logging

# Load environment variables
load_dotenv()

class Config:
    """Centralized configuration management for the application"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    
    # System Configuration
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    WORK_DIR = os.getenv("WORK_DIR", "./coding")
    
    # Performance Settings
    TIMEOUT = int(os.getenv("TIMEOUT", "600"))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    CACHE_SEED = int(os.getenv("CACHE_SEED", "42"))
    
    # Default max consecutive auto replies from .env
    DEFAULT_MAX_AUTO_REPLY = int(os.getenv("MAX_CONSECUTIVE_AUTO_REPLY", "10"))
    
    # Agent Configuration with dynamic values from .env
    AGENT_CONFIGS = {
        "planner": {
            "temperature": OPENAI_TEMPERATURE,
            "max_consecutive_auto_reply": DEFAULT_MAX_AUTO_REPLY,
            "max_tokens": 16384,  # GPT-4o mini limit
            "timeout": TIMEOUT
        },
        "coder": {
            "temperature": OPENAI_TEMPERATURE,
            "max_consecutive_auto_reply": DEFAULT_MAX_AUTO_REPLY // 2,  # Half of default
            "max_tokens": 16384,
            "timeout": TIMEOUT
        },
        "debugger": {
            "temperature": OPENAI_TEMPERATURE,
            "max_consecutive_auto_reply": DEFAULT_MAX_AUTO_REPLY // 3,  # Third of default
            "max_tokens": 16384,
            "timeout": TIMEOUT
        },
        "tester": {
            "temperature": OPENAI_TEMPERATURE,
            "max_consecutive_auto_reply": DEFAULT_MAX_AUTO_REPLY // 2,
            "max_tokens": 16384,
            "timeout": TIMEOUT
        },
        "executor": {
            "temperature": OPENAI_TEMPERATURE,
            "max_consecutive_auto_reply": DEFAULT_MAX_AUTO_REPLY // 3,
            "max_tokens": 16384,
            "timeout": TIMEOUT
        }
    }
    
    # LLM Default Configuration
    DEFAULT_LLM_CONFIG = {
        "request_timeout": 600,
        "seed": 42,
        "temperature": OPENAI_TEMPERATURE,
        "config_list": [{
            "model": OPENAI_MODEL,
            "api_key": OPENAI_API_KEY,
            "base_url": "https://api.openai.com/v1"
        }]
    }
    
    @classmethod
    def get_openai_config(cls) -> Dict[str, Any]:
        """
        Get base OpenAI configuration.
        
        Returns:
            Dict containing OpenAI configuration
        """
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
            
        return cls.DEFAULT_LLM_CONFIG
    
    @classmethod
    def get_agent_config(cls, agent_type: str) -> Dict[str, Any]:
        """
        Get agent-specific configuration.
        
        Args:
            agent_type: Type of agent (planner, coder, debugger, etc.)
            
        Returns:
            Dict containing agent configuration merged with base config
        """
        base_config = cls.get_openai_config()
        agent_config = cls.AGENT_CONFIGS.get(agent_type, {})
        
        return {
            **base_config,
            **agent_config
        }
    
    @classmethod
    def get_logging_config(cls) -> Dict[str, Any]:
        """
        Get logging configuration.
        
        Returns:
            Dict containing logging configuration
        """
        return {
            "level": getattr(logging, cls.LOG_LEVEL.upper()),
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    
    @classmethod
    def get_code_execution_config(cls) -> Dict[str, Any]:
        """
        Get code execution configuration.
        
        Returns:
            Dict containing code execution settings
        """
        return {
            "work_dir": cls.WORK_DIR,
            "use_docker": False,  # Can be made configurable via .env if needed
            "timeout": cls.TIMEOUT
        }
    
    @classmethod
    def validate_config(cls) -> None:
        """
        Validate the configuration.
        
        Raises:
            ValueError: If required configuration is missing or invalid
        """
        required_vars = [
            ("OPENAI_API_KEY", cls.OPENAI_API_KEY),
            ("OPENAI_MODEL", cls.OPENAI_MODEL)
        ]
        
        for var_name, var_value in required_vars:
            if not var_value:
                raise ValueError(f"Required configuration {var_name} is missing")
        
        # Validate model-specific constraints
        if cls.OPENAI_MODEL == "gpt-4o-mini":
            for agent_type, config in cls.AGENT_CONFIGS.items():
                if config.get("max_tokens", 0) > 16384:
                    raise ValueError(f"max_tokens for {agent_type} exceeds GPT-4o mini limit of 16384")
        
        # Validate work directory
        work_dir = Path(cls.WORK_DIR)
        if not work_dir.exists():
            work_dir.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def initialize(cls) -> None:
        """Initialize and validate configuration"""
        cls.validate_config()
        
        if cls.DEBUG_MODE:
            print("\n=== Configuration Initialized ===")
            print(f"Model: {cls.OPENAI_MODEL}")
            print(f"Temperature: {cls.OPENAI_TEMPERATURE}")
            print(f"Work Directory: {cls.WORK_DIR}")
            print(f"Log Level: {cls.LOG_LEVEL}")
            print(f"Request Timeout: {cls.DEFAULT_LLM_CONFIG['request_timeout']}s")
            print(f"Base URL: {cls.DEFAULT_LLM_CONFIG['config_list'][0]['base_url']}")
            print("===============================\n")

# Initialize configuration when module is imported
Config.initialize() 