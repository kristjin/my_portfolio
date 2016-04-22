#!/bin/python3

import sys


time = input().strip()
meridian = time[len(time)-2]
oldHour = int(time[0:2])
etc = time[2:len(time)-2]

if meridian == "A":
    if oldHour == 12:
        newHour = "00"
    else:
        newHour = str(oldHour)
else:
    newHour = oldHour+12
    if newHour == 24:
        newHour = "12"
    else: 
        newHour = str(newHour)

newTime = newHour+etc
print(newTime)
