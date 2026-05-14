#!/usr/bin/env python3

import sys
import ft_filter

length: int


def is_valid_string(s: str) -> bool:
    """
    is_valid_string(string) -> bool
    Return True if the string is longer than a given length, False otherwise.
    """
    return len(s) > length


def filterstring():
    """
    filterstring() -> list
    Filter the strings that are longer than a given length.
    """
    splited: list = sys.argv[1].split(" ")
    filtered: list = ft_filter.ft_filter(is_valid_string, splited)
    print(filtered)


def assertionError():
    """
    assertionError() -> None
    Print an error message and exit the program.
    """
    print("AssertionError: the arguments are bad")
    sys.exit(1)


def main():
    """
    main() -> None
    Main function to run the program.
    """
    if len(sys.argv) != 3:
        assertionError()

    try:
        global length
        length = int(sys.argv[2])
    except ValueError:
        assertionError()

    filterstring()


if __name__ == "__main__":
    main()
