#!/usr/bin/env python3
"""
Module that provides a function to create a multiplier function.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies by a given float."""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
