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
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
