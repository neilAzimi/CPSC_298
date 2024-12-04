import time
import logging
from functools import wraps
from typing import Any, Callable, Dict

logger = logging.getLogger(__name__)

def measure_time(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        
        logger.debug(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

class PerformanceMonitor:
    """Monitor performance metrics for the system"""
    
    def __init__(self):
        self.start_time = time.time()
        self.metrics: Dict[str, Any] = {}
    
    def get_timestamp(self) -> float:
        """Get current timestamp"""
        return time.time()
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        current_time = self.get_timestamp()
        
        self.metrics.update({
            'uptime': current_time - self.start_time,
            'timestamp': current_time
        })
        
        return self.metrics
    
    def record_metric(self, name: str, value: Any) -> None:
        """Record a new metric"""
        self.metrics[name] = value