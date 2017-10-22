import pytest


def test_series_sum():
    """Tests at the nth of 1."""
    from sum_terms import series_sum
    n = 1
    assert series_sum(n) == "1.00"


def test_series_sum2():
    """Tests at the nth of 2."""
    from sum_terms import series_sum
    n = 2
    assert series_sum(n) == "1.25"


def test_series_sum3():
    """Tests at the nth of 3."""
    from sum_terms import series_sum
    n = 3
    assert series_sum(n) == "1.39"


def test_series_sum4():
    """Tests at the nth of 4."""
    from sum_terms import series_sum
    n = 4
    assert series_sum(n) == "1.49"


def test_series_sum5():
    """Tests at the nth of 0."""
    from sum_terms import series_sum
    n = 0
    assert series_sum(n) == "0.00"


def test_series_sum6():
    """Tests at the nth of 10."""
    from sum_terms import series_sum
    n = 10
    assert series_sum(n) == "1.81"


def test_series_sum7():
    """Tests at the nth of 50."""
    from sum_terms import series_sum
    n = 50
    assert series_sum(n) == "2.35"