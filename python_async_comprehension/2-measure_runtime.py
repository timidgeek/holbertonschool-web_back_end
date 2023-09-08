#!/usr/bin/env python3
"""Task 2"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures and returns total runtime after four
    executions of `async_comprehension`
    """
    start: float = time.time()
    runner = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*runner)
    return (time.time() - start)
