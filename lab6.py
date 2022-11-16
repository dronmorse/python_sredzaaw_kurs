#!/usr/bin/python3

import os, urllib.request

URLs = [
    {'name':'mobilo', 'url':'http://www.mobilo24.eu/'},
    {'name':'nonexistent', 'url':'http://abc.cde.fgh.ijk.pl/'}, 
    {'name':'kursy', 'url':'http://www.kursyonline24.eu/'} ]
data_dir = r"C:\Users\Open-E\Desktop\scripts\GIT_repositories\python_sredzaaw_kurs"

for i in URLs:
    path = "%s\%s.html" %(data_dir, i['name']) 
    print (path)
    try:
        urllib.request.urlretrieve(i['url'], path)
        print ("done")
    except:
        print ("an error occured. Check if the page exists and try again")
        break
else:
    print ("all htmls were downlaoded successfully")





