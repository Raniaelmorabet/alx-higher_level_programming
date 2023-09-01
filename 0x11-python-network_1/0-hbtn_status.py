#!/usr/bin/python3

"""Fetches https://intranet.hbtn.io/status"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
