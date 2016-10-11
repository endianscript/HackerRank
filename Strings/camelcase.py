#!/bin/python3

import sys


s = input().strip()
if len(s) > 0:
    count = 1
else:
    count = 0

for index,i in enumerate(s):
    if s[index].isupper():
        count += 1
print (count)
