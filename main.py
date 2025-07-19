import sys
from stats import (
    get_num_words, 
    get_chars_dict, 
    get_sort_count
    )


def main():
    book_path = sys_argv()
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sort_count(chars_dict)
    print_report(book_path, num_words, sorted_chars)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    
def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at:", book_path)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for char, count in sorted_chars:
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    print("---------------END---------------")


def sys_argv():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1] 


main()