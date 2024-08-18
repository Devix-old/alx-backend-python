#!/usr/bin/env python3
"""
Module that provides a function to sum a list of integers as floats.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[int]) -> float:
    """Sums a list of integers as floats."""
    return float(sum(mxd_lst))
