#!/usr/bin/env python3

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gencon = ((a,b) for a in ports for b in ports)
counter = 0
for i in gencon:
    print (i)
    counter +=1
print ("Amount of connections: {}".format(counter))

gencon = ((a,b) for a in ports for b in ports if a != b)
counter = 0
for i in gencon:
    print (i)
    counter +=1
print ("Amount of connections: {}".format(counter))

gencon = ((a,b) for a in ports for b in ports if a < b)
counter = 0
for i in gencon:
    print (i)
    counter +=1
print ("Amount of connections: {}".format(counter))
