"""Kata: Sum of Two Lowest Positive Integers  - Finds and adds the two lowest positive integers
#1 Best Practices Solution by danman1979 and a lot more

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""

def sum_two_smallest_numbers(numbers):
    """This will find the sum of the two lowest ints in a string."""
    x = sorted(numbers)[:2]
    return x[0] + x[1]
