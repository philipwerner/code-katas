"""Test module for highest scoring word."""
import pytest
from highest_scoring_word import high


def test_highest():
    """First codewars test."""
    x = 'man i need a taxi up to ubud'
    assert high(x) == 'taxi'


def test_highest2():
    """Second test from codewars."""
    x = 'what time are we climbing up the volcano'
    assert high(x) == 'volcano'


def test_highest3():
    """Third test from codewars."""
    x = 'take me to semynak'
    assert high(x) == 'semynak'


def test_highest4():
    """First new test."""
    x = 'making up sentences is very hard'
    assert high(x) == 'sentences'


def test_highest5():
    """Second new test."""
    x = 'i really do not like coming up with these'
    assert high(x) == 'really'


def test_highest6():
    """Third new test."""
    x = 'TesT UsIng A MIX of uPPeR and LOWer cASEs'
    assert high(x) == 'uPPeR'


def test_highest7():
    """Test the same word in upper, lower and mixed."""
    x = 'TEST test TeSt'
    assert high(x) == 'TEST'


def test_highest8():
    """Test the same word in upper, lower and mixed in new order."""
    x = 'test TeSt TEST'
    assert high(x) == 'test'


def test_highest9():
    """Test the same word in upper, lower and mixed in new order."""
    x = 'TeSt test TEST'
    assert high(x) == 'TeSt'