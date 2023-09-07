#!/usr/bin/env python3
"""Task 9"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate functions parameters and return values
    with appropriate types. Which may or may not be given.
    """
    return [(i, len(i)) for i in lst]
