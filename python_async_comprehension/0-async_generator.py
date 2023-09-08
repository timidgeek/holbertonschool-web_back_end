#!/usr/bin/env python3
"""Task 0"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine, that takes no arguments, loops ten times,
    asynchronously waits 1 second, then uses the random module
    to yield a number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
