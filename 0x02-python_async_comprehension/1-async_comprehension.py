#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async_comprehension function"""
    return [i async for i in async_generator()]
