#!/usr/bin/python3
"""post an email"""


from urllib.request import urlopen, Request
from urllib.parse imparse import urlencode
import sys


if __name__ == "__main__":
    x = urlencode({"email": sys.argv[2]}).encode("ascii")
    y = Request(sys.argv[1], x)
    with urlopen(y) as z:
        print(z.read().decode("utf-8"))
