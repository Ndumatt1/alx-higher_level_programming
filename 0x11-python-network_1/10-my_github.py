#!/usr/bin/python3
'''
This module takes user github credentials and uses github API to display id
'''
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def func():
    auth = HTTPBasicAuth(argv[1], argv[2])
    with requests.get('https://api.github.com/user', auth=auth) as response:
        try:
            value = response.json()['id']
            print(value)
        except KeyError:
            return None


if __name__ == '__main__':
    func()
