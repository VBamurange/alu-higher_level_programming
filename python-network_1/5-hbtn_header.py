#!/usr/bin/python3
"""response header value"""


import requests
import sys


if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    y = x.headers.get("X-Request-Id")
    print(y)
