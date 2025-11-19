#!/usr/bin/env python3


import requests

resp = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t -type:", type(resp.text))
print("\t -content:", resp.text)
