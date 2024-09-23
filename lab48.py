#!/usr/bin/env python3

import csv
    
with open('lab48.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    for row in csvreader:
#        print('|'.join(row))
#    print(next(csvreader))
#    print(next(csvreader))
#    print(next(csvreader))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break