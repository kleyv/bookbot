def count_words(text):
    counter = 0
    lines = text.split('\n') 
    for line in lines:
        words = line.split(' ')
        for word in words:
            if len(word) > 0:
                counter += 1
    return counter

def count_chars(text): 
    words = text.split()
    counter = 0
    dic = {}
    for word in words:
        chars = list(word)
        for char in chars:
            char = char.lower()
            if char in dic:
                dic[str(char)] += 1
            else:
                dic[str(char)] = 1
                counter += 1
    return dic  
