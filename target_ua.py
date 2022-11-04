"""
Target Ukr version
"""

from random import choice

def generate_grid():
    """
    This function generates 5 unique letters.
    >>> len(generate_grid()) == 5
    True
    """
    alphabet = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї\
, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я'
    letters = alphabet.split(", ")
    # print(letters)
    result = []

    while len(result) < 5:
        letter = choice(letters)
        if letter not in result:
            result.append(letter)

    return result

def make_pair(dict_line):
    """
    Function return word and his part of language.
    >>> make_pair("авдіювати /v1.cf.advp :imperf:ua_2019")
    ('авдіювати', 'verb')
    >>> make_pair("авантюрниця /n10.p1.ko.<")
    ('авантюрниця', 'noun')
    """
    dict_line = dict_line.split(" ")[0:2]
    if len(dict_line) <= 1:
        return ()

    word, language_part = dict_line

    if language_part.startswith("noninfl"):
        return ()

    if language_part.startswith("noun") or\
    language_part.startswith("/n") or language_part.startswith("n"):
        return (word, "noun")

    if language_part.startswith("v") or language_part.startswith("/v"):
        return (word, "verb")

    if language_part.startswith("adj") or language_part.startswith("/adj"):
        return (word, "adjective")

    if language_part.startswith("adv") or language_part.startswith("/adv"):
        return (word, "adverb")

    return ()

def get_words(filename, letters):
    """
    Reads and sorts words from dictionary.
    >>> get_words("base.lst", [])
    []
    """
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            pair = make_pair(line.lower().strip())

            if not pair:
                continue
            if len(pair[0]) > 5 or (pair[0][0].lower() not in letters):
                continue

            words.append(pair)

    return words
