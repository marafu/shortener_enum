#!/usr/bin/python3
import string
import random
import urllib3
import sys

def wordlist_generation(size=5, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def main(target):
    count = 0
    while True:

        url = f'http://{target}/{wordlist_generation()}'
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        
        status_code = response.status

        if status_code == 302:
            print(f'{url} - {status_code}\n\n - {response.headers}\n\n')
        
        print(f'{url} - {status_code}\n\n - {response.headers}\n\n')


if __name__=="__main__":
	
	target = sys.argv[1]
	main(target)
