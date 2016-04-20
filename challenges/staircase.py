#!/bin/python3

import sys


n = int(input().strip())

for y in range(1, n+1):
    for i in range(n-y, 0, -1):
        print(' ',sep='',end='')
    for x in range(0, y):
        print('#',sep='',end='')
    print('','',end='\n')