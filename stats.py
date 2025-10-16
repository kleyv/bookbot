def count_words(text):
    counter = 0
    lines = text.split('\n') 
    for line in lines:
        words = line.split(' ')
        for word in words:
            if len(word) > 0:
                counter += 1
    return counter
 
