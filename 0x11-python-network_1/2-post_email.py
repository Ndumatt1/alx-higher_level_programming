#!/usr/bin/python3
'''
This module takes in a URL and email, sends a post request to the passed URL
with the email as a parameter and displays the body of the response
'''
if __name__ == '__main__':
    import urllib.request
    from sys import argv
    import urllib.parse

    value = {'email': argv[2]}
    email = urllib.parse.urlencode(value)
    email = email.encode('ascii')
    post_request = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(post_request) as response:
        body = response.read().decode('utf-8')
        print(body)
