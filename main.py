from stats import count_words
from stats import get_chars_dictionary 
from stats import sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = ''
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    #self.assertIsNotfilepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
#    print(f"Found {count_words(text)} total words")
    #print(text.split())
    chars = get_chars_dictionary(text)
    sorted_chars = sort_chars(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char}: {sorted_chars[char]}")
    print("============= END ===============")
main()

