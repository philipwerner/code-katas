"""String Pyramid code challenge for EC."""


def watch_pyramid_from_the_side(characters):
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
    if not characters:
        return characters
    c = len(characters)
    rows = []

    for i in range(c):
        num_repeat = (c - (i + 1)) * 2 + 1
        pre_pend = ''
        post_pend = ''
        if i > 0:
            pre_pend = characters[:i]
            post_pend = characters[0:i][::-1]
        rows.append(pre_pend + characters[i] * num_repeat + post_pend)

    for row in rows[::-1][1:]:
        rows.append(row)
    return '\n'.join(rows)


def count_visible_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    c = len(characters)
    side = (c - 1) * 2 + 1
    visible_charac = side ** 2
    return visible_charac


def count_all_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    c = len(characters)

    sum = 0
    for level in range(1, c + 1):
        side = (level - 1) * 2 + 1
        sum += side ** 2
    return sum