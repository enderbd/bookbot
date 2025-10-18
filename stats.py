def get_words_count(book_text):
    words_count = len(book_text.split())
    return words_count


def get_characters_count(book_text):
    characters_count = {}
    for char in book_text:
        if char.lower() in characters_count:
            characters_count[char.lower()] += 1
        else:
            characters_count[char.lower()] = 1

    return characters_count


def sort_on(items):
    return items["num"]


def get_sorted_chars(character_count):
    converted_to_list = [
        {"char": f"{char}", "num": num} for char, num in character_count.items()
    ]
    converted_to_list.sort(reverse=True, key=sort_on)
    return converted_to_list
