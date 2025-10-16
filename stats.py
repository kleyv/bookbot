def count_words(text):
    words = text.split() 
    return len(words)

def sort_on(items):
    return items["count"]

def sort_chars(d):
    sorted_chars = []
    for key in d:
        if key.isalpha():
            new_d = {'char':key, 'count': d[key]}
            sorted_chars.append(new_d)
    sorted_chars.sort(reverse=True,key=sort_on)
    sorted_dictionary = {}
    for dictionary in sorted_chars:
        key = dictionary['char']
        value = dictionary['count']
        sorted_dictionary[key] = value
    return sorted_dictionary

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
