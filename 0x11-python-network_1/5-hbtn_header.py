#!/usr/bin/python3
'''
This module takes in a URL, sends a request and display the value
of X-Request-Id in the response header
'''
if __name__ == '__main__':
    import requests
    from sys import argv

    with requests.get(argv[1]) as response:
        value = response.headers
        if 'X-Request-Id' not in value.keys():
            pass
        print(value['X-Request-Id'])
