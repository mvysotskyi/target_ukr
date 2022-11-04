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

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks user types words.
    >>> check_user_words(["предмет", "проданий"], "noun"\
    , ["п"], [("предмет", "noun"), ("поле", "noun")])
    (['предмет'], ['поле'])
    """
    valid_dict_words = [word[0] for word in dict_of_words if word[1] == language_part]
    valid_user_words = [
        word for word in user_words if (word in valid_dict_words) and (word[0] in letters)]
    return valid_user_words, [word for word in valid_dict_words if word not in valid_user_words]


def main():
    """
    Main game function.
    """
    language_parts = (('noun', "іменників"), ('verb', "дієслів"),\
    ('adjective', "прикметників"), ('adverb', "прислівників"))
    game_field = generate_grid()

    language_part = choice(language_parts)

    print(f"Ігрове поле: {game_field}")
    print(f"Введіть щонайменше 5 {language_part[1]},\n\
які починаються із букв ігрового поля: ")

    user_words = []
    while inp := input(">>> "):
        user_words.append(inp)

    if len(user_words) < 5:
        print("Ви ввели менше 5 слів. Бувайте!")

    dict_words = get_words("base.lst", game_field)
    correct_words, missed_words = check_user_words(user_words, language_part[0],
    game_field, dict_words)

    print(f"Ви ввели правильно: {', '.join(correct_words)}")
    print(f"Ви пропустили: {', '.join(missed_words)}")

if __name__ == "__main__":
    main()
