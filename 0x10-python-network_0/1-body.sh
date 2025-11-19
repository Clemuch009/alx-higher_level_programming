#!/usr/bin/bash

# Fetch the status code
status=$(curl -s -o body.txt -w "%{http_code}" "$1")

# Check if status is 200
if [ "$status" -eq 200 ]; then
    # Print the saved body
    cat body.txt
else
    echo "Request failed with status $status"
fi

# Clean up
rm body.txt

