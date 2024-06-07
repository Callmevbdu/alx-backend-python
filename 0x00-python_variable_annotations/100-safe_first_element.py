#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists, otherwise
    returns None.

    Parameters:
    lst (Sequence[Any]): A sequence of any type.

    Returns:
    Union[Any, None]: The first element of the sequence if it exists,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
