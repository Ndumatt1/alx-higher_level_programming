#!/usr/bin/python3
'''
This module takes user github credentials and uses github API to display id
'''
if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    auth = HTTPBasicAuth(argv[1], argv[2])
    with requests.get('https://api.github.com/user', auth=auth) as response:
        value = response.json()['id']
        print(value)
