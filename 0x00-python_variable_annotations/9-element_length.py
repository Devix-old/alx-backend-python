#!/usr/bin/env python3
"""
Module that provides a function to return list of sequences and their lengths.
"""


import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]) -> typing.List[
            typing.Tuple[typing.Sequence, int]]:
    """Returns list of sequences and their lengths."""
    return [(i, len(i)) for i in lst]
