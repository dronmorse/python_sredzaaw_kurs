#!/usr/bin/env python3

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)
print(f("long"))

print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))
