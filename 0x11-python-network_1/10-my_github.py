#!/usr/bin/python3
"""Connect to Github using Github Api
   Args:
       username: str
       password: PAT
   Return: user id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    basic = HTTPBasicAuth(username, password)
    req = requests.get(f'https://api.github.com/users/{username}', auth=basic)
    data = req.json()
    print(str(data["id"]))
