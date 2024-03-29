#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as req:
        res = req.read()
        print("Body response: \
        \n\t- type: {}\n\t- content: {} \
        \n\t- utf8 content: {}".format(
            type(res),
            res,
            res.decode('UTF-8')
            ))
