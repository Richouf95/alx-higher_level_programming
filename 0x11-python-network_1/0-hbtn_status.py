#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as req:
        res = req.read()
        print("Body response:")
        print("    - type: {}".format(type(res)))
        print("    - content: {}".format(res))
        print("    - utf8 content: {}".format(res.decode('UTF-8')))
