#!/usr/bin/python3
"""
Fetches content from url
display content
"""

import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.reason)
