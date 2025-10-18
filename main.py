import sys

from stats import get_characters_count, get_sorted_chars, get_words_count


def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words_count = get_words_count(book_text)
    characters_count = get_characters_count(book_text)
    characters_sorted = get_sorted_chars(characters_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char_dict in characters_sorted:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")


main()
