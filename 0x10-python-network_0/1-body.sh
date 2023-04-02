#!/bin/bash
# This script takes in a URL, sends a GET request to the URL
curl -s -w "%{http_code}\n" -o /dev/null -L "$1" | grep -q 200 && curl -s -L "$1"
