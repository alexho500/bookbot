def get_num_words(file_contents):
    nt = file_contents.split()
    return len(nt)


def get_num_char(file_contents):
    characters = { }
    file_contents = file_contents.lower()
    for char in file_contents:
        if char == " ":
            continue
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters


def dict_chars_count(file_contents):
    char_counts = get_num_char(file_contents)
    list_char = list(char_counts.items())
    list_char = sorted(char_counts.items(), key = lambda tup: tup[1], reverse=True)
    
    return list_char

