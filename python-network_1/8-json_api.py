#!/usr/bin/python3
"""search api"""


import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) == 2 else ""
    x = "http://0.0.0.0:5000/search_user"
    y = requests.post(x, data={'q' : q})
    try:
        y_dict = r.json()
        id, name = y_dict.get('id'), y_dict.get("name")
        if len(y_dict) == 0 or not id or not name:
            print('No result')
        else:
            print("[{}] {]".format(y_dict.get('id'), y_dict.get('name')))
    except:
        print("Not a valid JSON")
