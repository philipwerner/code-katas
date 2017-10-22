import pytest


def test_sum_two_smallest_numbers():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [5, 8, 12, 18, 22]
    assert sum_two_smallest_numbers(numbers) == 13


def test_sum_two_smallest_numbers2():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [7, 15, 12, 18, 22]
    assert sum_two_smallest_numbers(numbers) == 19


def test_sum_two_smallest_numbers3():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [25, 42, 12, 18, 22]
    assert sum_two_smallest_numbers(numbers) == 30


def test_sum_two_smallest_numbers4():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [250, 142, 120, 8, 122]
    assert sum_two_smallest_numbers(numbers) == 128


def test_sum_two_smallest_numbers5():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [2500, 422, 45, 189, 223]
    assert sum_two_smallest_numbers(numbers) == 234


def test_sum_two_smallest_numbers6():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [67, 900, 678, 1, 2]
    assert sum_two_smallest_numbers(numbers) == 3


def test_sum_two_smallest_numbers7():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [2522200, 423, 120000, 1898]
    assert sum_two_smallest_numbers(numbers) == 2321


def test_sum_two_smallest_numbers8():
    """Finds the sum of the two lowest positive ints."""
    from sum_of_two_lowest import sum_two_smallest_numbers
    numbers = [345, 4321, 864, 96310, 9999999]
    assert sum_two_smallest_numbers(numbers) == 1209
