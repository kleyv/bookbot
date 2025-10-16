def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def count_words(text):
    counter = 0
    # split by break lines
    lines = text.split('\n') 
    for line in lines:
        words = line.split(' ')
        # print(words)
        for word in words:
            if len(word) > 0:
                counter += 1
    return counter
    
def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    print(f"Found {count_words(text)} total words")
main()

