import pytest


def test_sum_two_smallest_numbers():
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [5, 8, 12, 18, 22]
    assert sum_two_smallest_numbers(numbers) == 13


def test_sum_two_smallest_numbers2():
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [7, 15, 12, 18, 22]
    assert sum_two_smallest_numbers(numbers) == 19


def test_sum_two_smallest_numbers3():
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [25, 42, 12, 18, 22]
    assert sum_two_smallest_numbers(numbers) == 30