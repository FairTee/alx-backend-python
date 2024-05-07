#!/usr/bin/env python3

"""
Measure Runtime Module
----------------------

This module provides a coroutine called measure_runtime that executes
async_comprehension four times in parallel using asyncio.gather, measures
the total runtime, and returns it.

Example:
    async def main():
        return await measure_runtime()

    print(asyncio.run(main()))

"""

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure Runtime Coroutine

    This coroutine executes async_comprehension four times in parallel using
    asyncio.gather, measures the total runtime, and returns it.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    return end_time - start_time
