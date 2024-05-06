#!/usr/bin/env python3
"""
Module for creating asyncio tasks for concurrent waiting.
"""

import asyncio
from typing import List
from functools import partial

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio tasks for wait_random and gather their results.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = []
    task_list = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(task_list):
        delay = await task
        delays.append(delay)
    return delays
