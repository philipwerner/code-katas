import pytest


def test_sum_no_duplicate():
    """Tests for a sum of 5 from list l."""
    from sum_a_list import sum_no_duplicates
    l = [1, 1, 2, 3]
    assert sum_no_duplicates(l) == 5


def test_sum_no_duplicate2():
    """Tests for a sum of 3 from list l."""
    from sum_a_list import sum_no_duplicates
    l = [1, 1, 2, 2, 3]
    assert sum_no_duplicates(l) == 3


def test_sum_no_duplicate3():
    """Tests for a sum of 13 from list l."""
    from sum_a_list import sum_no_duplicates
    l = [1, 1, 2, 3, 8, 9, 9]
    assert sum_no_duplicates(l) == 13


def test_sum_no_duplicate4():
    """Tests for a sum of 27 from list l."""
    from sum_a_list import sum_no_duplicates
    l = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8]
    assert sum_no_duplicates(l) == 27


def test_sum_no_duplicate5():
    """Tests for a sum of 6 from list l."""
    from sum_a_list import sum_no_duplicates
    l = [0, 1, 2, 3]
    assert sum_no_duplicates(l) == 6


def test_sum_no_duplicate6():
    """Tests for a sum of 45 from list l."""
    from sum_a_list import sum_no_duplicates
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sum_no_duplicates(l) == 45

