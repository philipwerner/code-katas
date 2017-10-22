import pytest


def test_arithmetic_progression():
    """This checks output will start at 1 and progress by 2 for 5 instances."""
    from arithmetic_progression import arithmetic_sequence_elements
    a = 1
    r = 2
    n = 5
    assert arithmetic_sequence_elements(a, r, n) == '1, 3, 5, 7, 9'


def test_arithmetic_progression2():
    """This checks output will start at 5 and progress by 5 for 5 instances."""
    from arithmetic_progression import arithmetic_sequence_elements
    a = 5
    r = 5
    n = 5
    assert arithmetic_sequence_elements(a, r, n) == '5, 10, 15, 20, 25'


def test_arithmetic_progression3():
    """This checks output will start at 2 and progress -1 by for 10 instances."""
    from arithmetic_progression import arithmetic_sequence_elements
    a = 2
    r = -2
    n = 10
    assert arithmetic_sequence_elements(a, r, n) == '2, 0, -2, -4, -6, -8, -10, -12, -14, -16'
   

def test_arithmetic_progression4():
    """This checks output will start at 10 and progress by -5 for 5 instances."""
    from arithmetic_progression import arithmetic_sequence_elements
    a = 10
    r = -5
    n = 5
    assert arithmetic_sequence_elements(a, r, n) == '10, 5, 0, -5, -10'


def test_arithmetic_progression5():
    """This checks output will start at 100 and progress by 100 for 6 instances."""
    from arithmetic_progression import arithmetic_sequence_elements
    a = 100
    r = 100
    n = 6
    assert arithmetic_sequence_elements(a, r, n) == '100, 200, 300, 400, 500, 600'


def test_arithmetic_progression6():
    """This checks output will start at -25 and progress by 25 for 10 instances."""
    from arithmetic_progression import arithmetic_sequence_elements
    a = -25
    r = 25
    n = 10
    assert arithmetic_sequence_elements(a, r, n) == '-25, 0, 25, 50, 75, 100, 125, 150, 175, 200'
