#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine called
async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async comprehensing over
async_generator, then return the 10 random numbers.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous function that collects 10 random numbers using an async
    comprehension over async_generator.
    Returns:
        List[float]: A list of 10 random floats.
    """
    return [i async for i in async_generator()]
