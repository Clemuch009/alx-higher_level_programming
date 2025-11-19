#!/usr/bin/bash
status=$(curl -s -o body.txt -X POST -H "Content-Type: application/json"-d'{"email": "test@gmail.com", "subject":"I will always be here for PLD"}' -w '%{http_code}' "$1")
if [ "$status" -eq 200 ]; then
	cat body.txt
fi
rm body.txt
