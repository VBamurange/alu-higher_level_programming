#!/usr/bin/python3
"""response header value"""


import urllib.request
import sys


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as arg:
        hum = arg.headers.get("X-Request-Id")
        print (hum)
