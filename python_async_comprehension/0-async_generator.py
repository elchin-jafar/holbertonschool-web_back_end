#!/usr/bin/env python3
"""async generator that loops 10 times"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield number in range 0-10 with 1sec delay"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
