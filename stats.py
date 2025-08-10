def get_num_words(words):
    return len(words.split())

def count_char(words):
    char_count = {}
    words = words.lower()
    for word in words:
        
        if word in char_count:
            char_count[word] = char_count[word]+1
        else:
            char_count[word] = 1
    return char_count
    