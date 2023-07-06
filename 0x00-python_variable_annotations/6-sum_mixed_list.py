#!/usr/bin/env python3
""" THis func takes list input of integers and floats, returns float """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums the list of integers and floats """
    return sum(mxd_lst)
