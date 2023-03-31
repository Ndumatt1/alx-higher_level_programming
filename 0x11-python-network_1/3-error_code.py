#!/usr/bin/python3
'''
This module takes in an URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
'''
if __name__ == '__main__':
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            decode_response = response.read().decode('utf-8')
            print(decode_response)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
