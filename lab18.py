#!/usr/bin/env python3

def double(x):
    return 2*x
     
def square(x):
    return x**2
     
def negative(x):
    return -x
     
def div2(x):
    return x/2

number = 8

#transformations = [double,square,div2,negative]
transformations = [square,square,div2,double]

tmp_return_value = number

for command in transformations:
    tmp_return_value = command(tmp_return_value)
    print(tmp_return_value)