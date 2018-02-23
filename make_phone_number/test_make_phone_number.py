"""Test module for create phone number."""
import pytest
from make_phone_number import phone


def test_short_list():
    """Test for error with a short list."""
    x = [1, 2, 3]
    with pytest.raises(ValueError):
        phone(x)


def test_long_list():
    """Test for error with a long list."""
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
    with pytest.raises(ValueError):
        phone(x)


def test_normal_list():
    """Test a valid list input."""
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert phone(x) == "(123) 456-7890"