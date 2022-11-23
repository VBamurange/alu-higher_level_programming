#!/usr/bin/python3
"""post an email"""


import requests
import sys


if __name__ == "__main__":
    x = {"email": sys.argv[2]}
    y = requests.post(sys.argv[1], data=x)
    print("{}".format(y.text))
