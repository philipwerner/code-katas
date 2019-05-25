"""String Pyramid code challenge for EC."""


def watch_pyramid_from_the_side(characters):
    """Side view of the pyramid."""
    if not characters:
        return characters
    characters = characters[::-1]
    length = len(characters)
    rows = []

    for i in range(length):
        empty_space = length - (i + 1)
        num_repeat = (i * 2) + 1
        rows.append(' ' * empty_space + characters[i] * num_repeat + ' ' * empty_space)
    return '\n'.join(rows)


def watch_pyramid_from_above(characters):
    """Top view of the pyramid."""
    if not characters:
        return characters
    c = len(characters)
    rows = []

    for i in range(c):
        num_repeat = (c - (i + 1)) * 2 + 1
        pre = ''
        post = ''
        if i > 0:
            pre = characters[:i]
            post = characters[0:i][::-1]
        rows.append(pre + characters[i] * num_repeat + post)

    for row in rows[::-1][1:]:
        rows.append(row)
    return '\n'.join(rows)


def count_visible_characters_of_the_pyramid(characters):
    """Count of visible letters."""
    if not characters:
        return -1
    c = len(characters)
    side = (c - 1) * 2 + 1
    visible = side ** 2
    return visible


def count_all_characters_of_the_pyramid(characters):
    """Count all characters in the pyramid."""
    if not characters:
        return -1
    c = len(characters)

    sum = 0
    for l in range(1, c + 1):
        side = (l - 1) * 2 + 1
        sum += side ** 2
    return sum
