#!/usr/bin/env python3
"""
a type-annotated function floor which takes a float n as argument and returns
the floor of the float.
"""


def floor(n: float) -> int:
    """Get the floor of a float number n.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of n.
    """
    return int(n // 1)
