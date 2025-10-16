from stats import count_words

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    print(f"Found {count_words(text)} total words")
main()

