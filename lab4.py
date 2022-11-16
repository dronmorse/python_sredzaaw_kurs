#!/usr/bin/python3

import os

def create_file_and_count_words(source):
    if os.path.isfile(source):
        print ("file already exists")
    else:
        print ("file not found. Creating...")    
        file = open('what_i_see', "w")
        file.write("it is quite cloudy and the weather is depressing")
        print("file created")
    file_read = open("what_i_see", "r")
    text = file_read.read()
    ind_words = text.split()
    num = len(ind_words)
    return num

source = r"C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs\what_i_see"
#os.remove(path)

print (create_file_and_count_words(source))
    







