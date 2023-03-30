#!/bin/bash
# This script take in an URL and displays all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" | grep -i allow | awk '{print}'
