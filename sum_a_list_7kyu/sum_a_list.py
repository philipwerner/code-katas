"""Kata: Sum a List But Ignore Any Duplicates  - Finds the sum of a
list while ignoring any duplicated numbers
#1 Best Practices Solution by zebulan, ExhaleO2, DCoulter

from collections import Counter


def sum_no_duplicates(nums):
    return sum(k for k, v in Counter(nums).items() if v == 1)
"""


def sum_no_duplicates(l):
    """This will find the sum of non repeated ints."""
    dup = list([x for x in l if l.count(x) < 2])
    answer = sum(dup)
    return answer
