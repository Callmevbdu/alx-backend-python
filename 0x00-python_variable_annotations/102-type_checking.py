#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and apply any necessary
changes.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array.

    Parameters:
    lst (Tuple): A tuple.
    factor (int): The zoom factor.

    Returns:
    List: A zoomed in version of the array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Change this to a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))  # Convert the float to an int
