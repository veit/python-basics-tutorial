"""Reads a file or stdin and returns the number of lines, words and characters –
similar to the UNIX wc utility."""

import sys


def main():
    """Count the occurrences of lines, words and characters in a file or
    stdin."""
    # initialize counts
    line_count = 0
    word_count = 0
    char_count = 0
    filename = None
    option = None
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        if params[0].startswith("-"):
            # If there are several parameters, the first one is taken as an option
            option = params.pop(0).lower().strip()
        if params:
            filename = params[0]
    file_mode = "r"
    if option == "-c":
        file_mode = "rb"
    if filename:
        infile = open(filename, file_mode)
    else:
        infile = sys.stdin
    with infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
    if option in ("-c", "-m"):
        print(f"{filename} has {char_count} characters.")
    elif option == "-w":
        print(f"{filename} has {word_count} words.")
    elif option == "-l":
        print(f"{filename} has {line_count} lines.")
    else:
        # print the answers using the format() method
        print(
            f"{filename} has {line_count} lines, {word_count} words and {char_count} characters."
        )


if __name__ == "__main__":
    main()
