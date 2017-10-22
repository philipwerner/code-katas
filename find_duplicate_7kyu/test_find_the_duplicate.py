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


def test_find_dup4():
    """Tests for duplicate of 78."""
    from find_the_duplicate import find_dup
    arr = [56, 5, 6, 78, 7, 8, 78]
    assert find_dup(arr) == 78


def test_find_dup5():
    """Tests for duplicate of 2."""
    from find_the_duplicate import find_dup
    arr = [0, 99, 1, 98, 2, 97, 2]
    assert find_dup(arr) == 2


def test_find_dup6():
    """Tests for duplicate of 10."""
    from find_the_duplicate import find_dup
    arr = [10, 11, 12, 13, 14, 15, 16, 17, 10]
    assert find_dup(arr) == 10