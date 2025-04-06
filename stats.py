def get_num_words(file_text):
    x = file_text.split() 
    y = len(x)
    return y


def character_count(text_to_count):
    alphabet_dict = {}
    b = text_to_count.lower()
    for character in b:
        if character in alphabet_dict:
            alphabet_dict[character] += 1
        else:
            alphabet_dict[character] = 1

    return alphabet_dict

def pretty_print(dict):
    for i,j in dict.items():
        print(f"{i}:{j}")