#################################
###Advent of Code Day 3
###Start Time: 9:53pm
###End Time: 11:27pm
###Author: Jonathan LeFeber
###Lines of Code: 
#################################

import time
lines = open("Puzzle3Input", "r").read().split("\n")
for y in range(len(lines)):
    lines[y] = list(lines[y])
   
#print(lines)
width = len(lines[0])
height = len(lines)
#print("Width:",width," Height:",height)

#Part 1
#Work line by line
#REMINDER, coords are in Y/X
'''
numStart=0#???
y=0
calculated=0
symbolList = ['-','+','!','@','#','$','%','^','&','*','/','?','=']
while y < height:
    print("******\nChecking Line:",y,"\n*****")
    x=0
    while x < width:
        if lines[y][x].isdigit():
            numStart = x
            while x+1 < width:
                if lines[y][x+1].isdigit():
                    x += 1
                    numEnd = x
                else:
                    numEnd = x
                    break
            #print("Debug:",lines[y][numStart:numEnd+1],y,numStart,numEnd)
            num = int(''.join(str(e) for e in lines[y][numStart:numEnd+1]))
            #print("Found number: ",num)
            #Search around number for symbol
            checking = True
            while checking:
                #Check above
                if y-1 > 0:
                    if numStart-1 > 0:
                        if lines[y-1][numStart-1] in symbolList:
                            calculated += num
                            print("Found Symbol for ",num,":",lines[y-1][numStart-1]," (Upper Left)")
                            break
                    for check in range(len(str(num))):
                        if lines[y-1][numStart+check] in symbolList:
                            calculated += num
                            print("Found Symbol for ",num,":",lines[y-1][numStart+check]," (Above)")
                            checking = False
                            break
                    if numEnd+1 < width:
                        if lines[y-1][numEnd+1] in symbolList:
                            calculated += num
                            print("Found Symbol for ",num,":",lines[y-1][numEnd+1]," (Upper Right)")
                            break
                #Check before/after
                if numStart-1 > 0:
                    if lines[y][numStart-1] in symbolList:
                        calculated += num
                        print("Found Symbol for ",num,":",lines[y-1][numStart-1]," (Left)")
                        break
                if numEnd+1 < width:
                    if lines[y][numEnd+1] in symbolList:
                        calculated += num
                        print("Found Symbol for ",num,":",lines[y-1][numStart+check]," (Right)")
                        break
                #Check below
                if y+1 < height:
                    if numStart-1 > 0:
                        if lines[y+1][numStart-1] in symbolList:
                            calculated += num
                            print("Found Symbol for ",num,":",lines[y+1][numStart-1]," (Lower Left)")
                            break
                    for check in range(len(str(num))):
                        if lines[y+1][numStart+check] in symbolList:
                            calculated += num
                            print("Found Symbol for ",num,":",lines[y+1][numStart+check]," (Below)")
                            checking = False
                            break
                    if numEnd+1 < width:
                        if lines[y+1][numEnd+1] in symbolList:
                            calculated += num
                            print("Found Symbol for ",num,":",lines[y+1][numEnd+1]," (Lower Right)")
                            break
                #Did not find symbol
                if checking:
                    print("Did not find symbol for: ",num)
                break
        x += 1
    y += 1
'''

#Part 2
#Change logic; find *, then check around for numbers. ONLY IF THERE ARE 2, then find number and multiply


print("Calculated! ",calculated)
print("\n",time.process_time())
