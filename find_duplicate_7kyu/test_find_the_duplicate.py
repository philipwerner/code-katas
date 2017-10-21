import pytest


def test_find_dup():
    """Tests for duplicate of 1."""
    from find_the_duplicate import find_dup
    arr = [5, 4, 3, 2, 1, 1]
    assert find_dup(arr) == 1


def test_find_dup2():
    """Tests for duplicate of 5."""
    from find_the_duplicate import find_dup
    arr = [1, 3, 2, 5, 4, 5, 7, 6]
    assert find_dup(arr) == 5

def test_find_dup3():
    """Tests for duplicate of 4."""
    from find_the_duplicate import find_dup
    arr = [4, 5, 6, 1, 2, 3, 4, 11, 12, 13, 14]
    assert find_dup(arr) == 4