#!/bin/bash
# This script takes an URL and sends a JSON post request to the URL passed
curl -s -X post --data @"$2" "$1"
