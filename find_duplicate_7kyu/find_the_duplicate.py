"""Kata: Find the Duplicated Number in a Consecutive Unsorted List  - Finds and returns
the duplicated number from the list
#1 Best Practices Solution by SquishyStrawberry

def find_dup(arr):
    return (i for i in arr if arr.count(i) > 1).next()
"""


def find_dup(arr):
    """This will find the duplicated int in the list"""
    dup = set([x for x in arr if arr.count(x) > 1])
    answer = list(dup)
    return answer[0]
