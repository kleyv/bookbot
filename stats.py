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

def get_chars_dictionary(text): 
    dictionary = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in dictionary:
            dictionary[lowered_char] += 1
        else:
            dictionary[lowered_char] = 1
    return dictionary
