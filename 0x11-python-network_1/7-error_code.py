#!/usr/bin/python3
'''
This module take in a URL, sends a request to the URL and displays
the body of the eresponse
'''
if __name__ == '__main__':
    import requests
    from sys import argv

    with requests.get(argv[1]) as response:
        if (response.status_code >= 400):
            print(f'Error code: {response.status_code}')
        else:
            print(response.text)
