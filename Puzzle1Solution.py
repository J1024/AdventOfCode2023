#################################
###Advent of Code Day 1
###Start Time: 7:45pm
###End Time: 8:41pm
###Author: Jonathan LeFeber
###Lines of Code: 132
#################################

import time
lines = open("Puzzle1Input", "r").read().split("\n")
for y in range(len(lines)):
    lines[y] = list(lines[y])
#print(lines)

'''
#FirstPart
calculated = 0
for line in lines:
    x = 0
    y = len(line)-1
    result = ""
    while(x<=y):
        if line[x].isdigit():
            result = line[x]
            break
        x = x+1
    while (y>=0):
        if line[y].isdigit():
            result = result + line[y]
            break
        y = y-1
    calculated = calculated + int(result)
print("Part 1: ",calculated,"\n")
'''            
        
#SecondPart
calculated = 0
for line in lines:
    x = 0
    y = len(line)-1
    result = ""
    while(x<=y):
        if line[x].isdigit():
            result = line[x]
            break
        elif (line[x]+line[x+1]) in ["on","tw","th","fo","fi","si","se","ei","ni"]:
            wordNum = (line[x]+line[x+1]+line[x+2])
            match wordNum:
                case "one":
                    result = "1"
                    break
                case "two":
                    result = "2"
                    break
                case "thr":
                    if line[x+3] == "e":
                        if line[x+4] == "e":
                            result = "3"
                            break
                case "fou":
                    if line[x+3] == "r":
                        result = "4"
                        break
                case "fiv":
                    if line[x+3] == "e":
                        result = "5"
                        break
                case "six":
                    result = "6"
                    break
                case "sev":
                    if line[x+3] == "e":
                        if line[x+4] == "n":
                            result = "7"
                            break
                case "eig":
                    if line[x+3] == "h":
                        if line[x+4] == "t":
                            result = "8"
                            break
                case "nin":
                    if line[x+3] == "e":
                        result = "9"
                        break
        x = x+1
    while (y>=0):
        if line[y].isdigit():
            result = result + line[y]
            break
        elif (line[y]+line[y-1]) in ["en","ow","ee","ru","ev","xi","ne","th","en"]:
            wordNum = (line[y]+line[y-1]+line[y-2])
            match wordNum:
                case "eno":
                    result = result + "1"
                    break
                case "owt":
                    result = result + "2"
                    break
                case "eer":
                    if line[y-3] == "h":
                        if line[y-4] == "t":
                            result = result + "3"
                            break
                case "ruo":
                    if line[y-3] == "f":
                        result = result + "4"
                        break
                case "evi":
                    if line[y-3] == "f":
                        result = result + "5"
                        break
                case "xis":
                    result = result + "6"
                    break
                case "nev":
                    if line[y-3] == "e":
                        if line[y-4] == "s":
                            result = result + "7"
                            break
                case "thg":
                    if line[y-3] == "i":
                        if line[y-4] == "e":
                            result = result + "8"
                            break
                case "eni":
                    if line[y-3] == "n":
                        result = result + "9"
                        break
        y = y-1
    calculated += int(result)
print("Part 2: ",calculated,"\n")
print("\n",time.process_time())