#!/usr/bin/env python3

import functools
import time

@functools.lru_cache()
def fib(n):
        
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    
    return result
start = time.time()

for i in range (1,37):
    print("Iteration number: {}".format(i))
    print("Fibonacci series no. {} - {}".format(i,fib(i)))
    print("Time taken:{}".format(time.time()-start))

print(fib.cache_info())


