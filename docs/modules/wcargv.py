"""wc module. Contains function: words_occur()"""

import sys


def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    # Prompt user for the name of the file to use.
    file_name = sys.argv.pop()
    # Open the file, read it and store its words in a list.
    f = open(file_name, "r")
    word_list = f.read().split()
    f.close()
    # Count the number of occurrences of each word in the file.
    occurs_dict = {}
    for word in word_list:
        # increment the occurrences count for this word
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    # Print out the results.
    print(
        f"File {file_name} has {len(word_list)} words, "
        f"{len(occurs_dict)} are unique:"
    )
    print(occurs_dict)


if __name__ == "__main__":
    words_occur()
