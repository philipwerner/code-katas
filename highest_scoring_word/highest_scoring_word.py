"""Kata: Highest Scoring Word.

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to it's position in the
alphabet: a = 1, b = 2, c = 3 etc. You need to return the highest scoring
word as a string. If two words score the same, return the word that
appears earliest in the original string.
Top rated solution by: daddepledge

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
"""


def high(x):
    """Find the highest scoring word in a string."""
    best_word = ''
    best_value = 0
    words = x.split()
    for i in range(len(words)):
        temp_word = words[i].lower()
        cur = words[i]
        letters = list(temp_word)
        temp_value = 0
        for x in range(len(letters)):
            temp_value += (ord(letters[x]) - 96)
        if temp_value > best_value:
            best_value = temp_value
            best_word = cur

    return best_word
