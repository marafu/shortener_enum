#!/usr/bin/python3

import string
import random
import urllib3
import argparse

def wordlist_generation(size=5, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))

def enumerate_site(size_letters:int, target:str, attempt_number:int) -> str:
    
    count = 0
    
    while count < attempt_number:

        url = f'{target}/{wordlist_generation(size_letters)}'        
        
        http = urllib3.PoolManager()
        
        response = http.request('GET', url)

        status_code = int(response.status)

        if status_code == 200:
            print(type(response.data.decode('utf-8')))
        
        count = count + 1

def main():

    parser = argparse.ArgumentParser(description='Enumeration tool for link shortener site', conflict_handler='resolve')
    
    parser.add_argument('-a', '--attempts', help='Number of request attempts for the target domain', type=int)

    parser.add_argument('-t', '--target', help='Target domain for enumeration: http://example.com', type=str, required=True)

    parser.add_argument('-s', '--size', help='Size number of unique-key word', type=int)

    arguments = parser.parse_args()

    if not arguments.size:
        arguments.size = 5
    
    if not arguments.attempts:
        arguments.attempts = 10 
    
    print(arguments.target, arguments.size, arguments.attempts)

    enumerate_site(int(arguments.size), str(arguments.target), int(arguments.attempts))

if __name__=="__main__":
	main()
