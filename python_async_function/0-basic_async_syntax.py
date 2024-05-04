#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
        generate random float num in range 0-10
        wait for that generated number as time then return it
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
