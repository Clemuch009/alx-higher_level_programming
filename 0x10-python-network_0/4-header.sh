#!/usr/bin/bash
status=$(curl -s -o body.txt -w '%{http_code}' -H'{"X-School-User-Id": 98}' "$1")
if [ "$status"  -eq 200 ]; then
	cat body.txt
fi
rm body.txt
