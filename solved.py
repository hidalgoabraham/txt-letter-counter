import time

spanish_letters_set = "aábcdeéfghiíjklmnñoópqrstuúüvwxyz"


def counter(archive, set_of_letters):
    lines_count = 0
    words_count = 0
    letters_count = 0
    letters_info = {}
    excluded_characters = []
    initialtime = time.time()
    for line in archive:
        lines_count += 1
        line = line.strip().lower()
        words = line.split()
        words_count += len(words)
        for character in line.lower():
            if character in set_of_letters:
                letters_count += 1
                if character in letters_info:
                    letters_info[character]["count"] += 1
                else:
                    letters_info[character] = {"count": 1, "probability": None}
            else:
                if not character in excluded_characters:
                    excluded_characters.append(character)

    finaltime = time.time()
    elapsed_time_ms = round((finaltime - initialtime) * 1e3, 2)

    print(f"Search Elapsed Time: {elapsed_time_ms} ms")

    chars_in_set_but_not_in_archive = []
    for letter in set_of_letters:
        if (letter not in letters_info) and (letter not in chars_in_set_but_not_in_archive):
            chars_in_set_but_not_in_archive.append(letter)

    # Calculate and store probabilities
    for letter in letters_info:
        letters_info[letter]["probability"] = round(100 * letters_info[letter]["count"] / letters_count, 2)

    def get_letter_probability(letter):
        return letters_info[letter]["probability"]

    sorted_keys = sorted(letters_info.keys(), key=get_letter_probability, reverse=True)

    # sorted_keys = sorted(letters_info.keys(), key=lambda letter: letters_info[letter]["probability"], reverse=True)

    # Get the letters occurrences sorted by probability
    sorted_letters_info = {}
    for key in sorted_keys:
        sorted_letters_info[key] = letters_info[key]

    return lines_count, words_count, letters_count, sorted_letters_info, excluded_characters, chars_in_set_but_not_in_archive


if __name__ == "__main__":
    file_path = "./quijote.txt"
    archive = open(file_path, mode="r", encoding="utf-8")
    lines_count, words_count, letters_count, sorted_letters_info, excluded_characters, chars_in_set_but_not_in_archive = counter(archive, spanish_letters_set)
    print(f"Lines: {lines_count}")
    print(f"Words: {words_count}")
    print(f"Letters: {letters_count}")
    print("Sorted Letters Occurrence:")
    for key, value in sorted_letters_info.items():
        print(f"{key} -> {value}")

    print(f"Excluded Characters:\n{excluded_characters}")
    print(f"Characters in Valid Set but not in Archive:\n{chars_in_set_but_not_in_archive}")
