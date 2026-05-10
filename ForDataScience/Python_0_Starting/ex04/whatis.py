#!/usr/bin/env python3

import sys

if len(sys.argv) >= 2:
    s = sys.argv[1]
    if not (s.isdigit() or (s.startswith('-') and s[1:].isdigit())):
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

if len(sys.argv) == 2:
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
