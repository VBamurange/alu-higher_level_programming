#1/usr/bin/python3
"""error code"""


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as x:
            y = x.read()
            print(y.decode("utf-8"))
    except urllib.error.HTTPError as w:
        print("Error code: {}".format(w.code))

