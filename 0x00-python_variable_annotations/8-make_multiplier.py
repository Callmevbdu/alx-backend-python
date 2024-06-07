#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): A float to be used as the multiplier in the returned
    function.

    Returns:
    Callable[[float], float]: A function that multiplies a float by the given
    multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
