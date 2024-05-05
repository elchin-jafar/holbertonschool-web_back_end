#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
from asyncio import gather
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension 4 times parallel and measure runtime"""
    s = perf_counter()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    return perf_counter() - s
