#!/usr/bin/env python3
"""Module for creating asyncio tasks."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return a task for wait_random with max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
