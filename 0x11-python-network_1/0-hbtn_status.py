#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status.
"""


import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        res = req.read()
        print("Body response:")
        print("    - type: {}".format(type(res)))
        print("    - content: {}".format(res))
        print("    - utf8 content: {}".format(res.decode('UTF-8')))
