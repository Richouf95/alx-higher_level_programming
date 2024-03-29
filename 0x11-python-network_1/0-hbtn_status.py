#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        res = req.read()
        print("Body response:")
        print("    - type: {}".format(type(res)))
        print("    - content: {}".format(res))
        print("    - utf8 content: {}".format(res.decode('UTF-8')))
