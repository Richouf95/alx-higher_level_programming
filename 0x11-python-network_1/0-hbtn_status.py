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
        print("Body response:\
                \n\t- type: {}\n\t- content: {}\
                \n\t- utf8 content: {}".format(
                    type(res),
                    res,
                    res.decode('UTF-8')
                    ))
