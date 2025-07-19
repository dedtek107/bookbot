def get_num_words(text):
    words = text.split()
    return len(words)



def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sort_count(char_counts):
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars