#!/usr/bin /env python3

import time
import functools

def CreateTimeWrapper(func):
    def TimeWrapper(*args, **kwargs):
        start = time.time()
        called_func = func(*args, **kwargs)
        end = time.time()
        print("Seconds passed: {} seconds".format(end-start))
        return called_func
    return TimeWrapper

#@CreateTimeWrapper - this will cause the wrapper to be called each time a reccurency occurs - worse in this case!!
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

#get_sequence(1)

#WITHOUT FUNCTOOLS!
get_sequence_with_time = CreateTimeWrapper(get_sequence)

print(get_sequence_with_time(20))
