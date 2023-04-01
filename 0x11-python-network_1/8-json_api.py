#!/usr/bin/python3
'''
This module takes in a letter sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''
if __name__ == '__main__':
    from sys import argv
    import requests

    if len(argv) < 1:
        q = ""
    else:
        q = {'q': argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    with requests.post(url, data=q) as response:
        try:
            value = response.json()
        except json.JSONDecodeError:
            print('Not a valid JSON')
        if value:
            print(f"{[value['id']]} {value['name']}")
        else:
            print('No result')
