import pytest


def test_group_by_commas():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 1
    assert group_by_commas(n) == '1'


def test_group_by_commas2():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 10
    assert group_by_commas(n) == '10'


def test_group_by_commas3():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 100
    assert group_by_commas(n) == '100'


def test_group_by_commas4():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 1000
    assert group_by_commas(n) == '1,000'


def test_group_by_commas5():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 10000
    assert group_by_commas(n) == '10,000'


def test_group_by_commas6():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 100000
    assert group_by_commas(n) == '100,000'


def test_group_by_commas7():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 1000000
    assert group_by_commas(n) == '1,000,000'


def test_group_by_commas8():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 35235235
    assert group_by_commas(n) == '35,235,235'


def test_group_by_commas9():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 789067
    assert group_by_commas(n) == '789,067'


def test_group_by_commas10():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 1234567890
    assert group_by_commas(n) == '1,234,567,890'



def test_group_by_commas11():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 9876543219876
    assert group_by_commas(n) == '9,876,543,219,876'


def test_group_by_commas12():
    """Tests that commas are inserted properly."""
    from grouped_by_commas import group_by_commas
    n = 1357924680
    assert group_by_commas(n) == '1,357,924,680'

