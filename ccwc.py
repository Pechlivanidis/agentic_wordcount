#!/usr/bin/env python3
import sys


def count_bytes(filename):
    """Count the number of bytes in a file."""
    with open(filename, "rb") as f:
        return len(f.read())


def count_lines(filename):
    """Count the number of lines in a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_words(filename):
    """Count the number of words in a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return sum(len(line.split()) for line in f)


def count_characters(filename):
    """Count the number of characters in a file."""
    with open(filename, "rb") as f:
        return len(f.read().decode("utf-8"))


def main():
    if len(sys.argv) < 2:
        print("Usage: ccwc [-c|-l|-w|-m] [filename]", file=sys.stderr)
        sys.exit(1)

    # Check if first argument is an option or filename
    if sys.argv[1].startswith("-"):
        option = sys.argv[1]
        if len(sys.argv) < 3:
            print("Usage: ccwc [-c|-l|-w|-m] <filename>", file=sys.stderr)
            sys.exit(1)
        filename = sys.argv[2]
    else:
        # No option provided, use default (-c -l -w)
        option = None
        filename = sys.argv[1]

    if option == "-c":
        byte_count = count_bytes(filename)
        print(f"{byte_count} {filename}")
    elif option == "-l":
        line_count = count_lines(filename)
        print(f"{line_count} {filename}")
    elif option == "-w":
        word_count = count_words(filename)
        print(f"{word_count} {filename}")
    elif option == "-m":
        char_count = count_characters(filename)
        print(f"{char_count} {filename}")
    elif option is None:
        # Default: output lines, words, and bytes
        line_count = count_lines(filename)
        word_count = count_words(filename)
        byte_count = count_bytes(filename)

        # Calculate field width like wc does:
        # use the width of the largest number
        max_width = max(
            len(str(line_count)), len(str(word_count)), len(str(byte_count))
        )

        output = (
            f"{line_count:>{max_width}} "
            f"{word_count:>{max_width}} "
            f"{byte_count:>{max_width}} {filename}"
        )
        print(output)
    else:
        print(f"Unknown option: {option}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
