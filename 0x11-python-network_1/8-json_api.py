#!/usr/bin/python3

"""Module that sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        json = res.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
