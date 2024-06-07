#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations to the
function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with a key in a dictionary, or a default value
    if the key is not in the dictionary.

    Parameters:
    dct (Mapping): A dictionary.
    key (Any): A key.
    default (Union[T, None]): A default value.

    Returns:
    Union[Any, T]: The value associated with the key in the dictionary, or the
    default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
