#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""


import requests

if __name__ == "__main__":
    data = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(data.text.__class__))
    print("\t- content: {}".format(data.text))
