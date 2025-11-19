#!/usr/bin/env python3

import requests
import sys

resp = requests.get(sys.argv[1])
print(resp.headers.get('X-Request-Id'))
