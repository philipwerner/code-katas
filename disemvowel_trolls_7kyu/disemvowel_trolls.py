"""Kata: Disemvowel Trolls  - Finds and replaces vowels with blank space

REGEX FTW!!!! So much better in Python!

#1 Best Practices Solution by cvk77, zyrolasting, sneakybueno

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
"""
import re

def disemvowel(string):
    """This will replace any instance of vowels with blank space."""
    return re.sub(r"[aeiouAEIOU]", "", string)
