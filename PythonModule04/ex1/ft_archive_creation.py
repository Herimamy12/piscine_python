#!/usr/bin/env python3


class SVault:
    def __init__(self, path):
        self.path = path

    def save(self, data: str) -> None:
        try:
            print(f"Initializing new storage unit: {self.path}")
            with open(self.path, 'w') as f:
                print("Storage unit created successfully...\n")
                print("Inscribing preservation data...")
                for line in data:
                    print(line.strip())
                    f.write(line)
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{self.path}' ready for long-term preservation.")
        except Exception as e:
            print(f"ERROR: {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    vault = SVault('new_discovery.txt')
    data = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    vault.save(data)


if __name__ == '__main__':
    main()
