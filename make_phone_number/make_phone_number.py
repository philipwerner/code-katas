"""Create Phone Number Kata from Codewars."""


def phone(x):
    """Create the phone number."""
    if len(x) < 10:
        raise ValueError('List needs to contain 10 numbers')
    elif len(x) > 10:
        raise ValueError('List needs to contain 10 numbers')

    first = x[0:3]
    second = x[3:6]
    third = x[6:]
    area_code = ''
    mid = ''
    last = ''
    for i in range(len(first)):
        area_code = area_code + str(first[i])
        mid = mid + str(second[i])
    for x in range(len(third)):
        last = last + str(third[x])
    return "(" + area_code + ") " + mid + "-" + last
