#!/usr/bin/env python3

"""
Async Generator Module
----------------------

This module provides an asynchronous generator coroutine called async_generator
which yields random numbers between
0 and 10. It waits for 1 second asynchronously
before yielding each random number.

Example:
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())

"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
