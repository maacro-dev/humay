import time
from functools import wraps
import asyncio
from . import logger  

def time_check(func):

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        logger.info(f"Executing {func.__name__}...")
        try:
            result = await func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed_time_ms = (end_time - start_time) * 1000
            logger.info(f"{func.__name__} done in {elapsed_time_ms:.2f} ms")
        return result

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        logger.info(f"Executing {func.__name__}...")
        try:
            result = func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed_time_ms = (end_time - start_time) * 1000
            logger.info(f"{func.__name__} done in {elapsed_time_ms:.2f} ms")
        return result

    # Check if the function is asynchronous
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper
