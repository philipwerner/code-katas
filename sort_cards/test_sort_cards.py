"""The tests ran by codewars."""
from sort_cards import sort_cards
import pytest


def test_sort_first_set():
    """First test set from codewars."""
    test_set = '39A5T824Q7J6K'
    assert sort_cards(test_set) == list('A23456789TJQK')


def test_sort_second_set():
    """Second test set from codewars."""
    test_set = 'Q286JK395A47T'
    assert sort_cards(test_set) == list('A23456789TJQK')


def test_sort_third_set():
    """Third test set from codewars."""
    test_set = '54TQKJ69327A8'
    assert sort_cards(test_set) == list('A23456789TJQK')


def test_my_first():
    """My own test."""
    test_set = '9352KQA'
    assert sort_cards(test_set) == list('A2359QK')


def test_my_second():
    """My own test # 2."""
    test_set = 'KQ32T'
    assert sort_cards(test_set) == list('23TQK')


def test_my_third():
    """My own test."""
    test_set = 'TQ842AJ5'
    assert sort_cards(test_set) == list('A2458TJQ')
