def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    print(get_book_text(filepath))

main()

