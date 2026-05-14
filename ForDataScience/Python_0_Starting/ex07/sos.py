#!/usr/bin/env python3

import sys


def isnotalnumspace(s):
    """
    Checks if the character is not alphanumeric or space.
    """
    return not s.isalnum() and s != " "


def invalid_input():
    """
    Checks if the input is invalid.
    """
    if len(sys.argv) != 2:
        return True
    if any(isnotalnumspace(c) for c in sys.argv[1]):
        return True
    return False


def morse_code():
    """
    Converts the input string to Morse code.
    """
    morse_dict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        " ": "/ ",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    return "".join(morse_dict[c] for c in sys.argv[1].lower())


def main():
    """
    Main function.
    """
    if invalid_input():
        print("AssertionError: the arguments are bad")
        return

    print(morse_code())


if __name__ == "__main__":
    main()
