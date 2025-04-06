def get_num_words(file_text):
    x = file_text.split() 
    y = len(x)
    return y


def character_count(text_to_count):
    alphabet_dict = {}
    b = text_to_count.lower()
    for character in b:
        if character in alphabet_dict and character.isalpha():
            alphabet_dict[character] += 1
        else:
            alphabet_dict[character] = 1

    return alphabet_dict

def sort_characters(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    
    return chars_list