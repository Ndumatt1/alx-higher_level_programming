#!/usr/bin/python3
''' This python script fetches http://alx-intranet.hbtn.io/status '''

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        value = response.read()
        print('Body response:')
        print(f'\t- type: {type(value)}')
        print(f'\t- content: {value}')
        print(f"\t- utf8 content: {value.decode('utf-8')}")
