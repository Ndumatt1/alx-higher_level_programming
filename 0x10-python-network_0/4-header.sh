#!/bin/bash
# This script takes in a URL as an argument and sends a GET request
curl -s -H "X-School-User-Id: 98" "$1"
