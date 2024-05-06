#!/usr/bin/env python3
"""
Module for creating asyncio tasks.
"""

import asyncio
from typing import Union

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
