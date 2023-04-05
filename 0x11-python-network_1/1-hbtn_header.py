#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    content_type = response.getheader('X-Request-Id')
print(content_type)
