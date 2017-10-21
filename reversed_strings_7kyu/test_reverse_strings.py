import pytest


def test_solution():
    """Will reverse string 'world' to 'dlrow'."""
    from reverse_strings import solution
    string = 'world'
    assert solution(string) == 'dlrow'


def test_solution2():
    """Will reverse string 'hello' to 'olleh'."""
    from reverse_strings import solution
    string = 'hello'
    assert solution(string) == 'olleh'


def test_solution3():
    """Will reverse string '' to ''."""
    from reverse_strings import solution
    string = ''
    assert solution(string) == ''


def test_solution4():
    """Will reverse string 'h' to 'h'."""
    from reverse_strings import solution
    string = 'h'
    assert solution(string) == 'h'


def test_solution5():
    """Will reverse string 'codefellows' to 'swollefedoc'."""
    from reverse_strings import solution
    string = 'codefellows'
    assert solution(string) == 'swollefedoc'


def test_solution6():
    """Will reverse string 'philip' to 'pilihp'."""
    from reverse_strings import solution
    string = 'philip'
    assert solution(string) == 'pilihp'


def test_solution7():
    """Will reverse string 'apple' to 'elppa'."""
    from reverse_strings import solution
    string = 'apple'
    assert solution(string) == 'elppa'


def test_solution8():
    """Will reverse string 'python' to 'nohtyp'."""
    from reverse_strings import solution
    string = 'python'
    assert solution(string) == 'nohtyp'