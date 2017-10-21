import pytest


def test_filter_list():
    """This checks a list of [1, 2, 'a', 'b']."""
    from list_filtering import filter_list
    l = [1, 2, 'a', 'b']
    assert filter_list(l) == [1, 2]


def test_filter_list2():
    """This checks a list of [1, 'a', 'b', 0, 15]."""
    from list_filtering import filter_list
    l = [1, 'a', 'b', 0, 15]
    assert filter_list(l) == [1, 0, 15]


def test_filter_list3():
    """This checks a list of [1, 2, 'aasf', '1', '123', 123]."""
    from list_filtering import filter_list
    l = [1, 2, 'aasf', '1', '123', 123]
    assert filter_list(l) == [1, 2, 123]
