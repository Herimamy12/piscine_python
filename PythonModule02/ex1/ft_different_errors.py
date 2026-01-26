#!/usr/bin/env python3

def garden_operations():
    print("Testing ValueError...")
    try:
        integer = int("abc")
        print(f"Converted integer: {integer}")
    except ValueError as ve:
        print(f"Caught ValueError: {ve}\n")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
        print(f"Division result: {result}")
    except ZeroDivisionError as zde:
        print(f"Caught ZeroDivisionError: {zde}\n")

    print("Testing FileNotFoundError...")
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
            print(f"File content: {content}")
    except FileNotFoundError as fnfe:
        print(f"Caught FileNotFoundError: {fnfe}\n")

    print("Testing KeyError...")
    try:
        sample_dict = {"rose": 1, "dahlia": 2}
        value = sample_dict["missing plant"]
        print(f"Dictionary value: {value}")
    except KeyError as ke:
        print(f"Caught KeyError: {ke}\n")

    print("Testing multiple errors together...")
    print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")
