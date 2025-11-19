#!/usr/bin/env python3

import sys
from urllib import request


with request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
