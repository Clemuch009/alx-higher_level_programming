#!/usr/bin/env python3

import sys
import requests

data = {"email": sys.argv[2]}
resp = requests.post(sys.argv[1], data=data)
print(resp.text)
