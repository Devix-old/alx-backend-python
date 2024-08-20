#!/usr/bin/env python3
"""Generate 10 randoms numbers using async function"""
from random import uniform
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """async_generator function()"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
