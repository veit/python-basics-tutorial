"""wc module. Contains function: words_occur()"""

from argparse import ArgumentParser


def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    parser = ArgumentParser()
    # Prompt user for the name of the file to use.
    parser.add_argument("-f", "--file", dest="filename", help="read data from the file")
    args = parser.parse_args()
    file_name = args.filename
    # Open the file, read it and store its words in a list.
    with open(file_name, "r") as f:
        word_list = f.read().split()
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
