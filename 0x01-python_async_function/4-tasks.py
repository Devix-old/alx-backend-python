#!/usr/bin/env python3
"""Module for handling async tasks."""
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Create n tasks with wait_random and return their results as a list.
    """
    return [await task_wait_random(max_delay) for _ in range(n)]
