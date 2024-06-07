#!/usr/bin/env python3
from typing import List
"""
a type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Sum the elements of a list of floats.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(input_list))
