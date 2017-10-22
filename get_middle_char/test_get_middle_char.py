import pytest


def test_get_middle():
    """Tests string 'test' for middle of 'es'."""
    from get_middle_char import get_middle
    s = "test"
    assert get_middle(s) == "es"


def test_get_middle2():
    """Tests string 'testing' for middle of 't'."""
    from get_middle_char import get_middle
    s = "testing"
    assert get_middle(s) == "t"


def test_get_middle3():
    """Tests string 'middle' for middle of 'dd'."""
    from get_middle_char import get_middle
    s = "middle"
    assert get_middle(s) == "dd"


def test_get_middle4():
    """Tests string 'A' for middle of 'A'."""
    from get_middle_char import get_middle
    s = "A"
    assert get_middle(s) == "A"


def test_get_middle5():
    """Tests string 'rabbits' for middle of 'b'."""
    from get_middle_char import get_middle
    s = "rabbits"
    assert get_middle(s) == "b"


def test_get_middle6():
    """Tests string 'codefellows' for middle of 'e'."""
    from get_middle_char import get_middle
    s = "codefellows"
    assert get_middle(s) == "e"


def test_get_middle7():
    """Tests string 'amazombie' for middle of 'o'."""
    from get_middle_char import get_middle
    s = "amazombie"
    assert get_middle(s) == "o"


def test_get_middle8():
    """Tests string 'alkaline' for middle of 'al'."""
    from get_middle_char import get_middle
    s = "alkaline"
    assert get_middle(s) == "al"


def test_get_middle9():
    """Tests string 'montypython' for middle of 'p'."""
    from get_middle_char import get_middle
    s = "montypython"
    assert get_middle(s) == "p"
