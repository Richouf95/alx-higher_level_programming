#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(
            sys.argv[1],
            urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
            )
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
