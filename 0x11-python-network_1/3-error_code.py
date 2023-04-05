#!/usr/bin/python3
"""
sends a request to the URL and
displays the body of the response
Return:
      Error code:
"""

import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(data)
    except HTTPError as e:
        print('Error code:', e.code)
