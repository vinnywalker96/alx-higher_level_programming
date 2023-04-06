#!/usr/bin/python3
"""
sends a request to the URL
and displays the value of the variable
Args:
    X-Request-Id
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers['X-Request-Id'])
