#!/usr/bin/env python3

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connection = []
connection = [(a,b) for a in ports for b in ports]
print ("1", len(connection))

connection = [(a,b) for a in ports for b in ports if a != b]
print ("2", len(connection))

connection = [(a,b) for a in ports for b in ports if a < b]
print ("3", len(connection))