#!/bin/bash
# This script takes an URL and sends a JSON post request to the URL passed
curl -s -X post -H "Content-Type: application/json" -data @"$2" "$1"
