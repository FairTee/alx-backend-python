#!/usr/bin/env python3

"""
Async Comprehension Module
---------------------------

This module provides an asynchronous coroutine called async_comprehension that
collects 10 random numbers using an async comprehension over async_generator.

Example:
    async def main():
        print(await async_comprehension())

    asyncio.run(main())

"""

import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async Comprehension Coroutine

    This coroutine collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [i async for i in async_generator()]
