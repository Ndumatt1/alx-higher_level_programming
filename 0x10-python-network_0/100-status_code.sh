#!/bin/bash
# This script takes in a URL, sends a request and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
