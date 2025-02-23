import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import num_of_words
from stats import character
from stats import sorted_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path to book>")
        sys.exit(1)

    filepath = sys.argv[1]
    char_count = character(filepath)

   #print(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_of_words(filepath)} total words") #display total word count
    sorted_chars = sorted_characters(char_count)
    for char, count in sorted_chars:
       print(f"{char}: {count}")


main()