#!/usr/bin/env python3
"""multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function which multiplies"""
    return lambda mltp: mltp * multiplier
