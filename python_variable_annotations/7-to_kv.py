#!/usr/bin/env python3
"""complex types"""
from typing import Union, Tuple

IntOrFloat = Union[int, float]


def to_kv(k: str, v: IntOrFloat) -> Tuple[str, float]:
    """return tuple"""
    return (k, v * v)
