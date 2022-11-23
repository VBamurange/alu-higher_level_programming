#!/usr/bin/python3
"""time for an interview"""


import sys
import requests


if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
        x = requests.get(url)
        y = x.json()
        for i in range(10):
            print("{}: {}".format(y[i]["sha"], y[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
