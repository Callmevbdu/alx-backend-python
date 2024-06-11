#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay and returns
a asyncio.Task.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task from a coroutine.
    This function takes an integer max_delay as an argument and returns an
    asyncio.
    Task. The asyncio.Task is created from the wait_random coroutine.
    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.
    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
