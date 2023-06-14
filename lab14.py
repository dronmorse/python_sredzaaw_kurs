#!/usr/bin/env pyton3

import os

files_to_process = [
    r"C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs\source_lab13_1.py",
    r"C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs\source_lab13_2.py"
    ]

for file in files_to_process:
    print("File: {}".format(os.path.basename(file)))
    with open(file, "r") as raw:
        source = raw.read()
        exec(source)
    
