#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import sys
import requests

if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        letter = ""
    else:
        letter = args[1]

    req = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={"q": letter}
            )

    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                res.get("id"),
                res.get("name")
                ))
    except ValueError:
        print("Not a valid JSON")
