#!/usr/bin/env python3

import sys


def print_result(s: str) -> None:
    """Print the result of the program."""
    print(f"The text contains {len(s)} characters.")
    print(f"{sum(1 for c in s if c.isupper())} upper letters")
    print(f"{sum(1 for c in s if c.islower())} lower letters")
    print(f"{sum(1 for c in s if not c.isalnum() and not c.isspace())} punctuation marks")
    print(f"{sum(1 for c in s if c.isspace())} spaces")
    print(f"{sum(1 for c in s if c.isdigit())} digits")


def main() -> None:
    """Main function of the program."""
    s: str
    if len(sys.argv) < 2:
        s = input("What is the text to count?\n")
        print(s)
    elif len(sys.argv) > 2:
        print("AssertionError: More than one argument are provided.")
        sys.exit(1)
    else:
        try:
            s = sys.argv[1]
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
    print_result(s)


if __name__ == "__main__":
    main()
