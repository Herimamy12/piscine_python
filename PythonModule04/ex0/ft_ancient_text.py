#!/usr/bin/env python3


import sys


class SVault:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            print(f"Accessing Storage Vault: {self.path}")
            with open(self.path, 'r') as f:
                print("Connection established...\n")
                content = f.read()
            print("RECOVERED DATA:\n", content, "\n", sep='')
            print("Data recovery complete.  Storage unit disconnected.")
        except FileNotFoundError:
            print("ERROR: File not found.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file_path>")
        return
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    vault = SVault(sys.argv[1])
    vault.load()


if __name__ == '__main__':
    main()
