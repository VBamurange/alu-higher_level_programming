#!/usr/bin/python3
"""what's my status"""


import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as link:
        see = link.read()
        print("Body response:")
        print("\t- type: ()".format(type(see)))
        print("\t- content: ()".format(see))
        print("\t- utf8 content: ()".format(see.decode("utf-8")))
