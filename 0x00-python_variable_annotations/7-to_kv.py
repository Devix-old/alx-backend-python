#!/usr/bin/env python3
"""
create a tuple from a string and the square of a number.
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Creates a tuple from a string and the square of a number."""
    return (k, v * v)
