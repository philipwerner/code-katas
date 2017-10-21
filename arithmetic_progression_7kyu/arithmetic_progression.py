
"""Kata: Arithmetic Progression - Return the 'n' elements of the sequence
with the given common difference 'r' and the first element 'a'
#1 Best Practices Solution by zebulan (there were a lot of others that wre similar)

def arithmetic_sequence_elements(a, r, n):
    return ', '.join(str(a + b * r) for b in xrange(n))
"""


def arithmetic_sequence_elements(a, r, n):
    """Will return arithmetic progression with 'a' as starting point and 'r' as common difference"""
    # Your code here!:)
    return ', '.join(str(a + b * r) for b in range(n))
