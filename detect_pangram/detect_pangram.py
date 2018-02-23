"""Kata: Detect Pangram - Check if input sentence is a pangram.

Best Practices Solution:
import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""
import re


def is_pangram(s):
    """Check for pangram."""
    x = s.lower()
    y = re.sub('[^A-Za-z]+', '', x)
    if len(set(y)) == 26:
        return True
    else:
        return False
