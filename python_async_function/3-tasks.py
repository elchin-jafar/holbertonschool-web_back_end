#!/usr/bin/env python3
"""tasks function return task"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task function return async task"""
    return asyncio.create_task(wait_random(max_delay))
