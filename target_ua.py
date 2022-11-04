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
