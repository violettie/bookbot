def count_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_characters(char_count):
    char_list = []
    for item in char_count:
        char_list.append({"char": item, "num": char_count[item]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list