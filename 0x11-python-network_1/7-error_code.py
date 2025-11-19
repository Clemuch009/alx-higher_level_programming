#!/usr/bin/env python3

import requests
import sys

resp = requests.get(sys.argv[1])
if resp.status_code >= 400:
    print("Error code:", resp.status_code)

else:
    print(resp.text)
