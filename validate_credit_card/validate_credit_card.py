"""Kata: Validate Credit Card  - Validates a credit card number."""


def validate(n):
    """Validate input of credit card, return True or False."""
    if n == [] or sum(n) == 0:
        return False
    elif len(n) % 2 == 0:
        a = n[::2]
        for i in range(len(a)):
            n[i * 2] = a[i] * 2
    else:
        a = n[1::2]
        cur = 1
        for i in range(len(a)):
            n[cur] = a[i] * 2
            cur = cur + 2
    for i in range(len(n)):
        if n[i] > 9:
            temp = []
            s = str(n[i])
            for d in s:
                temp.append(int(d))
            result = sum(temp)
            if result > 9:
                n[i] = n[i] - 9
            else:
                n[i] = result
    if sum(n) % 10 == 0:
        return True
    else:
        return False
