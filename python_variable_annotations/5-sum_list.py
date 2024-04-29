#!/usr/bin/env python3
"""takes input list return sum list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list elements"""
    sum: float = 0
    for input in input_list:
        sum += input
    return sum
