#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    asynchronous coroutine that takes in an integer argument,
    and waits for a random delay, and eventually returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
