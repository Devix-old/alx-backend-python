#!/usr/bin/env python3
"""
Module for random delay asynchronous functions.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
