#!/usr/bin/bash
status=$(curl -s -o body.txt -w "%{http_code}" "$1")
echo "$status"
rm body.txt
