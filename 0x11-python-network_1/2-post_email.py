#!/usr/bin/python3
"""sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, data) as response:
        retrieve_email = response.read().decode('utf-8')

    print(retrieve_email)
