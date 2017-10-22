"""Kata: Sum of the First nth Term of Series  - Returns the sum of following series upto nth term(parameter).

I previously solved this with JS, I really enjoy seeing the difference in the solution code
between the two languages

#1 Best Practices Solution by MMMAAANNN and others

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """This will return the sum of the nth term."""
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * float(i))
    answer = '%.2f' % sum
    return answer
