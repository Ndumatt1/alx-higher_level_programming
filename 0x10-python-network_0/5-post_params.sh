#!/bin/bash
# This script sends a post request to the passed URL
curl -s -X post --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
