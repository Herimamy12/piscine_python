#!/usr/bin/env python3


import sys


class SVault:
    def __init__(self, path):
        self.path = path

    def save(self, data: str) -> None:
        try:
            print("SECURE PRESERVATION:")
            with open(self.path, 'w') as f:
                for line in data:
                    print(line.strip())
                    f.write(line)
            print("Vault automatically sealed upon completion")
        except Exception as e:
            print(f"ERROR: {e}")

    def load(self):
        try:
            print("Initiating secure vault access...")
            with open(self.path, 'r') as f:
                print("Vault connection established with failsafe protocols\n")
                content = f.read()
            print("SECURE EXTRACTION:\n", content, "\n", sep='')
        except FileNotFoundError:
            print("ERROR: File not found.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file_path>")
        return
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    vault = SVault(sys.argv[1])
    vault.load()

    data = [
        "[CLASSIFIED] New security protocols archived"
    ]
    vault.save(data)
    print()
    print("All vault operations completed with maximum security.")


if __name__ == '__main__':
    main()
