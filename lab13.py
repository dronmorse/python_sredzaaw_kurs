#!/usr/bin/env python3

import math

formula = input("please input your mathematical formula, where x is your argument: ")

argument_list = []
value = 0
while value <= 10:
    argument_list.append(value)
    value += 0.1

for x in argument_list:
    print("{:5f}".format(x), "{:f}".format(eval(formula)))