#!/usr/bin/env python3


import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archID = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    if archID.strip() == "" or report.strip() == "":
        sys.stderr.write("No archivist ID or report provided. Exiting.\n")
        return
    print()
    print(f"[STANDARD] Archive status from {archID}: {report}")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels \
verified\n")
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
