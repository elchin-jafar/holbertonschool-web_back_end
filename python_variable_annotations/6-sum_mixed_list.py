#!/usr/bin/python3
"""sum mixed list"""
from typing import List, Union

UnionList = List[Union[int, float]]


def sum_mixed_list(mxd_list: UnionList) -> float:
    return float(sum(mxd_list))
