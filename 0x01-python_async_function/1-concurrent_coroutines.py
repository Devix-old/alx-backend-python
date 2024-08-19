#!/usr/bin/env python3
"""
Module to run multiple wait_random coroutines concurrently.
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Execute wait_random n times with max_delay and return the delays.
    """
    return [await wait_random(max_delay) for _ in range(n)]
