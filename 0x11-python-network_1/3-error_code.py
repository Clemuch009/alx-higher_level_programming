#!/usr/bin/env python3

from urllib import request
import sys
from urllib.error import HTTPError, URLError
try:
    with request.urlopen(sys.argv[1]) as response:
        body = response.read().decode('utf-8')
        print(body)
except HTTPError as e:
    print("Error code:", e.code)
except URLError as f:
    pass
