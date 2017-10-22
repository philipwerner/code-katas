"""Kata: Grouped By Commas  - Adds commas for every third int


#1 Best Practices Solution by mbaxa and others

def group_by_commas(n):
    return '{:,}'.format(n)
"""
def group_by_commas(n):
    """This add a comma at every third space when len is > 3."""
    answer = '{:,}'.format(n)
    return answer
