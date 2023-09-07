#!/usr/bin/env python3
"""Task 6"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    type-annotated function which takes a list of
    integers and floats, and returns their sum
    as a float
    """
    return sum(mxd_list)
