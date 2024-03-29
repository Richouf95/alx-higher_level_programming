#!/usr/bin/python3
"""
github commits
"""


import sys
import requests

if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2],
        sys.argv[1]
        ))

    commits_list = req.json()

    try:
        for x in range(10):
            print("{}: {}".format(
                commits_list[x].get("sha"),
                commits_list[x].get("commit").get("author").get("name")
                ))
    except IndexError:
        pass
