#!/usr/bin/python3
"""error code"""


import requests
import sys


if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    if x.status_code < 400:
        print(x.text)
    elif x.status_code >= 400:
        print("Error code: {}".format(x.status_code))
