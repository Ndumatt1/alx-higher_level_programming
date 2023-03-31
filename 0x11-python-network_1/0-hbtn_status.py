#!/usr/bin/python3
# This python script fetches http://alx-intranet.hbtn.io/status

if __name__ == '__main__':
    import urllib.request
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        value = response.read()
        print('Body response:')
        print('\t - type:', type(value))
        print('\t - content:', value)
        print('\t - utf8 content: OK')
