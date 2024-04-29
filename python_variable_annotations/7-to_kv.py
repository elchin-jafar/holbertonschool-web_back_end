#!/usr/bin/env python3
"""complex types"""
from typing import Union

IntOrFloat = Union[int, float]


def to_kv(k: str, v: IntOrFloat) -> tuple[str, IntOrFloat]:
    """return tuple"""
    return (k, v)
