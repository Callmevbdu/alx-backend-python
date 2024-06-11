#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.

    This function is nearly identical to wait_n, but it calls task_wait_random instead of wait_random.

    Args:
        n (int): The number of times to execute task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A sorted list of the wait times from each execution of task_wait_random.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
