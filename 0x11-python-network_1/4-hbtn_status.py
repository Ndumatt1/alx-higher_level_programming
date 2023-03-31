#!/usr/bin/python3
'''
This module fetches https://alx-intranet.hbtn.io/status using requests module
'''
if __name__ == '__main__':
    import requests

    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        value = response.text
        print('Body response:')
        print(f'\t- type: {type(value)}')
        print(f'\t- content: {value}')
