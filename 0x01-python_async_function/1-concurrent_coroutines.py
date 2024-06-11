#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written and
write an async routine called wait_n that takes in 2 int arguments (in this
order): n and max_delay. You will spawn wait_random n times with the specified
max_delay. wait_n should return the list of all the delays (float values). The
list of the delays should be in ascending order without using sort() because of
concurrency.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random` n times with the specified
    max_delay and returns the list of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for `wait_random`.

    Returns:
        List[float]: The list of all the delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for _ in range(n):
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)  # noqa
        for task in done:
            delays.append(task.result())
    return delays
