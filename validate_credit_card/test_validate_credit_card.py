"""Test module for Validate Credit Card module."""
import pytest
from validate_credit_card import validate


def test_input_empty_list_returns_false():
    """Test for False return from empty list input."""
    x = []
    invalid = False
    assert validate(x) == invalid


def test_input_list_of_one_number_returns_false():
    """Test for False return from list of one item."""
    x = [9]
    invalid = False
    assert validate(x) == invalid


def test_for_valid_card():
    """Test for a True response."""
    x = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    valid = True
    assert validate(x) == valid
