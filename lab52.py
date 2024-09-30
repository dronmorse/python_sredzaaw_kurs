#!/usr/bon.env python3

import os
import requests

def gen_get_files(dir):
    for file in os.listdir(dir):
        yield os.path.join(dir, file)

def gen_get_file_lines(filename):
    for file in filename:
        with open(file, 'r') as data:
            for line in data.readlines():
                yield line.strip('\n')

def check_webpage(url):
    for link in url:
        try:
            page = requests.get(url=link)
            if page.status_code == 200:
                yield True
        except:
            yield False

file = gen_get_files('c:/temp/links_to_check')
line = gen_get_file_lines(file)
webpage_gen = check_webpage(line)

for page in webpage_gen:
    print (page)