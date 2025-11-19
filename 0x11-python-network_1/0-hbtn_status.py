#!/usr/bin/env python3

from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    obj = response
    print(obj.headers)
    print(obj.info())
