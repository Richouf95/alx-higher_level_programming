#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""


import sys
import requests

if __name__ == "__main__":
    req = requests.post(
            sys.argv[1],
            data={"email": sys.argv[2]}
            )

    print(req.text)
