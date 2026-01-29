#!/usr/bin/env python3


class SVault:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            with open(self.path, 'r') as f:
                content = f.read()
            print("SUCCESS: Archive recovered - ''", content, "''", sep='')
            print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis1 = SVault("lost_archive.txt")
    crisis1.load()
    print()

    path = "../data-generator-tools/security_protocols.txt"
    print(f"CRISIS ALERT: Attempting access to '{path}'...")
    crisis1 = SVault(path)
    crisis1.load()
    print()

    path = "../data-generator-tools/standard_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{path}'...")
    crisis1 = SVault(path)
    crisis1.load()
    print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == '__main__':
    main()
