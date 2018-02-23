"""Test module for detect_pangram."""
import pytest
from detect_pangram import is_pangram as p


pangram = True
not_pangram = False


def test_a_pangram_for_true():
    """Test a known pangram that only contains letter."""
    x = 'the quick brown fox jumps over the lazy dog'
    assert p(x) == pangram


def test_a_pangram_for_true2():
    """Test a known pangram that only contains letter."""
    x = 'abcdefghijklmnopqrstuvwxyz'
    assert p(x) == pangram


def test_a_pangram_for_true_with_punctuation():
    """Test a known pangram that contains punctuation."""
    x = 'the quick, brown fox jumps over the lazy dog!!!'
    assert p(x) == pangram


def test_a_pangram_for_true_with_numbers_and_punctuation():
    """Test a known pangram that only contains text."""
    x = 'the 600 quick, brown fox 90909 jumps over 6667655 the lazy dog'
    assert p(x) == pangram


def test_a_pangram_with_mixed_upper_lower_cases():
    """Test a known pangram with mix of upper and lower cases."""
    x = 'The QUIck, BrOWn FOX jumpS oveR the LAzy dog!!'
    assert p(x) == pangram


def test_non_pangram_with_just_letters():
    """Test a non pangram for a False response."""
    x = 'this is not a pangram'
    assert p(x) == not_pangram
