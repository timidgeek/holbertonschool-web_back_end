#!/usr/bin/env python3
"""Task 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function that takes a float as an argument
    and returns a function that multiplies a float by that argument
    """
    def multiply(number: float) -> float:
        return (number * multiplier)

    return multiply
