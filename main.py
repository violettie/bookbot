from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha() == False:
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()