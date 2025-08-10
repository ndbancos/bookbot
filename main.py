from stats import get_num_words, count_char
import sys
if (len(sys.argv)<2):
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = get_book_text(sys.argv[1])
    count = get_num_words(words)
    char = count_char(words)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words" )
    print("--------- Character Count -------")
    for items in char:
        print(f"{items}: {char[items]}")


main()
