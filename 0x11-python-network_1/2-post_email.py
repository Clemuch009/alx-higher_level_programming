#!/usr/bin/env python3

import sys
from urllib import request
from urllib import parse

url = sys.argv[1]
email = sys.argv[2]
data = {"email": email}
info = parse.urlencode(data).encode()

req = request.Request(url, data=info)

with request.urlopen(req) as response:
    obj = response.read().decode('utf-8')
    print(obj)
