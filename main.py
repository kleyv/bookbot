from stats import count_words
from stats import count_chars

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
    for char in chars:
        print(f"'{char}': {chars[char]}")
main()

