#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up a list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
