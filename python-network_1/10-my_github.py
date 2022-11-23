#!/usr/bin/python3
"""my github"""


import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    x = 'https://api.github.com/user'
    user = sys.argv[1]
    y = sys.argv[2]
    z = HTTPBasicAuth(username=user, password=y)
    w = requests.get(x, auth=z)
    u = w.json()
    print(u.get('id'))
