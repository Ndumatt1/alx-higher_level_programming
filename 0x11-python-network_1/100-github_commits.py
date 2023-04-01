#!/usr/bin/python3
'''
This module lists 10 commits from github repository
'''
if __name__ == '__main__':
    from sys import argv
    import requests
    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    with requests.get(url) as request:
        values = request.json()
        for value in values[:10]:
            sha = value['sha']
            name = value['commit']['author']['name']
            print(f'{sha}: {name}')
