#!/usr/bin/env python3
"""Task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    type-annotated function which takes a string, and int OR float
    as arguments, and returns a tuple - starting with str `k`,
    ending with the square of int/float `v`, which shall be
    annotated as a float
    """
    return (k, float(v) ** 2)
