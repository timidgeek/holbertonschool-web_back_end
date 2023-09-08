#!/usr/bin/env python3
"""Task 1"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    spawn `wait_random` n times with the specified `max_delay`
    `wait_n` should return the list of all the delays (float values),
    in ascending order without using sort() because of concurrency
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
