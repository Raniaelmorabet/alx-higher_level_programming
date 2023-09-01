#!/usr/bin/python3

"""Module that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import sys

    url = sys.argv[1]
    with urlopen(Request(url)) as response:
        print(response.headers.get('X-Request-Id'))
