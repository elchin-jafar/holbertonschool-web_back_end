#!/usr/bin/env python3
"""wait_n with task_wait_random"""
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n with task_wait_random"""
    result: List = []
    for _ in range(n):
        result.append(await task_wait_random(max_delay))
    return sorted(result)
