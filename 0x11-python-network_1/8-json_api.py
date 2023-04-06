#!/usr/bin/python3
"""ends a POST request to http://0.0.0.0:5000/search_user
    with a letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post(url, data={'q': q})

    try:
        json_data = res.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
