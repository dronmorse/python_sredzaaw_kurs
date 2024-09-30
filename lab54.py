#!/usr/bin/env python3

import itertools as it
import os

def scantree(path):
    for file in os.scandir(path):
        if os.path.isdir(file) == True:
            yield file
            yield from scantree(file.path)
        else:
           yield file 

listing = []
for file in scantree(r"C:\temp"):
    listing.append(file)

for element in listing:
    print("Is it a directory: {} - Full path: {}".format(os.path.isdir(element), element.path))

listing_sorted = sorted(listing, key = lambda x: os.path.isdir(x))
listing_grouped = it.groupby(listing_sorted, key = lambda x: os.path.isdir(x))

for key, paths in listing_grouped:
    print("Is dir: {} - List {}".format(key, list(paths)))