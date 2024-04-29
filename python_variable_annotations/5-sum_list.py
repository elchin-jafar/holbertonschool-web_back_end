#!/usr/bin/python3
"""takes input list return sum list"""


def sum_list(input_list: list[float]) -> float:
    sum: float = 0
    for input in input_list:
        sum += input
    return sum
