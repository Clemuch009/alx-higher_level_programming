#!/usr/bin/bash
curl -si "$1" | grep -i content-length | awk '{print $2}'
