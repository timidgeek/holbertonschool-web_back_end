#!/usr/bin/env python3
"""Task 4"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    spawn `task_wait_random` n times with the specified `max_delay`
    `task_wait_n` should return the list of all the delays (float values),
    in ascending order without using sort() because of concurrency
    """
    tasks = [(task_wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
