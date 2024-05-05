#!/usr/bin/env python3
"""async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        collects 10 random numbers from async_generator of previous task
        then return these nums as list
    """
    return [i async for i in async_generator()]
