import sys
from stats import count_words
from stats import count_of_characters
from stats import sorted_list_of_dictionaries

def main(sysargv):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sysargv[1]}...")
    print("----------- Word Count ----------")
    num_words = count_words(sysargv[1])
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = sorted_list_of_dictionaries(sysargv[1])
    for dict in character_count:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv)