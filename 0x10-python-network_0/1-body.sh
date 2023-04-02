#!/bin/bash
# This script takes in a URL, sends a GET request to the URL
curl -s -w "%{http_code}\n" -o /dev/null "$1" | grep -q 200 && curl -s "$1"
