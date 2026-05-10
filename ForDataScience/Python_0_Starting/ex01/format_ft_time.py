#!/usr/bin/env python3
from datetime import datetime

date = datetime.now().timestamp()
scintificNotation = "{:.2e}".format(date)

print("Seconds since January 1, 1970:", date, "or",
      scintificNotation, "in scientific notation")

print(datetime.now().strftime("%b %d %Y"))
