"""Kata: Filtering Lists - Remove strings from a list of integers
#1 Best Practices Solution by clawtros & others (me too!)

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
"""

def filter_list(l):
    """return a new list with the strings filtered out"""
    return [i for i in l if not isinstance(i, str)]
