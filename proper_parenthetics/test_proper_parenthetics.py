"""Test module for proper parenthetics."""
import pytest
from proper_parenthetics import parens


def test_error_is_raised_when_invalid_input():
    """."""
    x = ''
    with pytest.raises(ValueError):
        parens(x)


def test_parens_on_balanced_input():
    """Test that a 0 is returned on a balanced string."""
    x = '()'
    assert parens(x) == 0


def test_parens_on_balanced_input_2():
    """Test that a 0 is returned on a balanced string."""
    x = '((((()))))'
    assert parens(x) == 0


def test_parens_on_unclosed_open_paren():
    """Test that 1 is returned when paren left open."""
    x = '('
    assert parens(x) == 1


def test_parens_on_unclosed_open_paren_2():
    """Test that 1 is returned."""
    x = '((((()))))(()'
    assert parens(x) == 1


def test_parens_on_unopened_closed_paren():
    """Test that -1 is returned when closed paren has no open."""
    x = ')'
    assert parens(x) == -1


def test_parens_on_unopened_closed_paren2():
    """Test that -1 is returned when closed paren has no open."""
    x = '(((())))))))'
    assert parens(x) == -1


def test_with_letters_in_string():
    """Test that 0 is returned with letters in string."""
    x = '((apples))'
    assert parens(x) == 0


def test_with_letters_in_string_2():
    """Test that 1 is returned with letters in string."""
    x = '((apples))(oranges'
    assert parens(x) == 1


def test_with_letters_in_string_3():
    """Test that -1 is returned with letters in string."""
    x = '((apples))(oranges))'
    assert parens(x) == -1
