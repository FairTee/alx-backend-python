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


async def async_generator() -> float:
    """
    Asynchronous Generator Coroutine

    This coroutine loops 10 times, each time asynchronously waits for 1 second,
    then yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    """
    Print Yielded Values Coroutine

    This coroutine prints the values yielded by async_generator.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
