#!/usr/bin/env python3

import itertools as it

def get_factors(x):
    
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


candidates = [i for i in range(1, 1001)]
filtered_list = it.filterfalse(lambda x: sum(get_factors(x)) != x, candidates)

for i in filtered_list:
    print("Perfect number: {} - Divisors: {}".format(i, get_factors(i)))


