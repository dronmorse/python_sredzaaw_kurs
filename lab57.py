#!/usr/bin/env python3

import os
import zipfile
import requests

class Zip_Download:
    
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        file = requests.get(self.url)
        if file.status_code == 200:
            with open(self.tmp_file, 'wb') as new_file: 
                new_file.write(file.content)
        return self
    
    def __exit__(self, type, value, traceback):
        print("File {} from {} has been successfully downloaded!".format(self.tmp_file, self.url))

with Zip_Download('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r'c:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(r"c:/temp")
        z.extract(a_file, '.', None)