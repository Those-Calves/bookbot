from stats import get_num_words, character_count, sort_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    
    text = get_book_text(path)
    print(text)
    a = get_num_words(text)
    print(f"Found {a} total words")
    count = character_count(text)
    sorted_list = sort_characters(count)
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")

main() 