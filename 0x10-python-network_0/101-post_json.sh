#!/usr/bin/bash
status=$(curl -s -o body.txt -X POST --data-binary @"$2" -H "Content-type: application/json" -w "%{http_code}" "$1")

cat body.txt
rm body.txt
