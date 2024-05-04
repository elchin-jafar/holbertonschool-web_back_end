#!/usr/bin/env python3
"""execute multiple coroutines"""
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines"""
    result: List = []
    for _ in range(n):
        result.append(await wait_random(max_delay))
    return sorted(result)
