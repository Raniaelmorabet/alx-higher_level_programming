#!/usr/bin/python3

"""Module that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    r = requests.post(url, data=values)
    print(r.text)
