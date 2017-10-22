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


def test_filter_list4():
    """This checks a list of [34, 87, '45', 'i', 89]."""
    from list_filtering import filter_list
    l = [34, 87, '45', 'i', 89]
    assert filter_list(l) == [34, 87, 89]


def test_filter_list5():
    """This checks a list of ['yes', 'no', 'maybe', 999]."""
    from list_filtering import filter_list
    l = ['yes', 'no', 'maybe', 999]
    assert filter_list(l) == [999]


def test_filter_list6():
    """This checks a list of [1, 2, 9, 8, '3', '4', '7', 6]."""
    from list_filtering import filter_list
    l = [1, 2, 9, 8, '3', '4', '7', 6]
    assert filter_list(l) == [1, 2, 9, 8, 6]


def test_filter_list7():
    """This checks a list of ['oh no']."""
    from list_filtering import filter_list
    l = ['oh no']
    assert filter_list(l) == []
