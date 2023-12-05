#################################
###Advent of Code Day 2
###Start Time: 8:53pm
###End Time: 9:30pm
###Author: Jonathan LeFeber
###Lines of Code: 95
#################################

import time
lines = open("Puzzle2Input", "r").read().split("\n")

'''
#Part 1
REDMAX = 12
GREENMAX = 13
BLUEMAX = 14
calculated = 0

for line in lines:
    idEnd = line.find(':')
    ID = int(line[5:idEnd])
    start = 0
    valid = True
    while(line.find('red',start) != -1):
        start = line.find('red',start)
        numStart = line.find(' ',start-5)
        num = line[numStart+1:start-1]
        #print("Red:",num)
        start += 1
        if int(num)>REDMAX:
            valid = False
            break
    start = 0
    while(line.find('green',start) != -1):
        start = line.find('green',start)
        numStart = line.find(' ',start-5)
        num = line[numStart+1:start-1]
        #print("Green:",num)
        start += 1
        if int(num)>GREENMAX:
            valid = False
            break
    start = 0
    while(line.find('blue',start) != -1):
        start = line.find('blue',start)
        numStart = line.find(' ',start-5)
        num = line[numStart+1:start-1]
        #print("Blue:",num)
        start += 1
        if int(num)>BLUEMAX:
            valid = False
            break
    if valid:
        calculated += ID
print("Part 1: ",calculated)
print("\n",time.process_time())
'''

#Part 2
REDMAX = 12
GREENMAX = 13
BLUEMAX = 14
calculated = 0

for line in lines:
    red = 0
    green = 0
    blue = 0
    start = 0
    while(line.find('red',start) != -1):
        start = line.find('red',start)
        numStart = line.find(' ',start-5)
        num = int(line[numStart+1:start-1])
        start += 1
        if num>red:
            red = num
    start = 0
    while(line.find('green',start) != -1):
        start = line.find('green',start)
        numStart = line.find(' ',start-5)
        num = int(line[numStart+1:start-1])
        start += 1
        if num>green:
            green = num
    start = 0
    while(line.find('blue',start) != -1):
        start = line.find('blue',start)
        numStart = line.find(' ',start-5)
        num = int(line[numStart+1:start-1])
        start += 1
        if num>blue:
            blue = num
    calculated += red*green*blue
print("Part 2: ",calculated)
print("\n",time.process_time())