#!/bin/bash
# THos script takes in an URL, sends a request to the URL and displays the size
curl -sI "$1" | grep -i content-length | awk '{print $2}'
