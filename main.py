from stats import get_num_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)
    a = get_num_words(text)
    print(f"{a} words found in the document")

main() 