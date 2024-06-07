#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with the
appropriate types:

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples. Each tuple contains a sequence from the input
    and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples. Each tuple contains a
    sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]
