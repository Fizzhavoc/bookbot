from stats import get_num_words
from stats import get_text_count
from stats import sort_counts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_contents = get_book_text(path)

    print("----------- Word Count ----------")
    num_words = get_num_words(book_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count = get_text_count(book_contents)

    char_list = sort_counts(char_count)
    for char_info in char_list:
        character=char_info["char"]
        if character.isalpha():
            print(f"{character}: {char_info['num']}")
    print("============= END ===============")
main()