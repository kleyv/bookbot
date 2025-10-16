from stats import count_words
from stats import count_chars
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
#    print(f"Found {count_words(text)} total words")
    #print(text.split())
    chars = count_chars(text)
    sorted_chars = sort_chars(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char}: {sorted_chars[char]}")
    print("============= END ===============")
main()

