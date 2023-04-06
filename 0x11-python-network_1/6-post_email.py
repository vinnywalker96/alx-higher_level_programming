#!/usr/bin/python3
"""sends a POST request to the passed URL with the email"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    res = requests.post(url, data)
    print(res.text)
