#!/usr/bin/python3
'''
This module takes in a URL and an email address, sends a POST request
to the URL with the email as a parameter and finally display the body
of the response
'''
if __name__ == '__main__':
    import requests
    from sys import argv

    email = {'email': argv[2]}
    with requests.post(argv[1], data=email) as response:
        print(response.text)
