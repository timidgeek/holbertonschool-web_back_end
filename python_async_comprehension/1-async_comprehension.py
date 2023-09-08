#!/usr/bin/env python3
"""Task 1"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine tha takes and returns 10 random numbers
    from the `async_generator`
    """
    return [number async for number in async_generator()]
