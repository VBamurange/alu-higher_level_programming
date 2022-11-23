#!/usr/bin/python3
"""my github"""


import requests
from  requests.auth import HTTPBasicAuth
import sys


x = 'https://api.github.com/user'
user = sys.argv[1]
y = sys.argv[2]
z = HTTPBaicAuth(username=user, password=y)
w = requests.get(x, v=z)
u = w.json()
print(u.get('id'))
