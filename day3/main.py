import os
from datetime import datetime

print('Hello, World!')

dirpath = os.getcwd()

with open(dirpath + '/day3/input.txt', 'r') as f:
    input = f.read().splitlines()

output = [0, 0]

# not the best way to solve the problem
# intersection() function compares 2 array to get the intersection
# but the way it did is by looping through each value which is very inefficient
# tooks ~10mins for the program to finish

def makeWire(index, length, axis, step):
    for i in range(length):
        if axis == "x":
            cur[0] += step
        else:
            cur[1] += step
        wire[index].append(list(cur))

def intersection(lists): 
    return [value for value in lists[0] if value in lists[1]] 

def closest(arr):
    for index, val in enumerate(arr):
        arr[index] = abs(val[0]) + abs(val[1])

    return min(arr)

def shortestpath(arr):
    for index, val in enumerate(arr):
        arr[index] = wire[0].index(val) + wire[1].index(val) + 2

    return min(arr)


cur = [0, 0]

input[0] = input[0].split(',')
input[1] = input[1].split(',')

wire = [[], []]

print("Start: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("Creating Wire 1: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

for val in input[0]:
    direction = val[0:1]
    length = int(val[1:])

    if direction == "R":
        makeWire(0, length, "x", 1)
    elif direction == "L":
        makeWire(0, length, "x", -1)
    elif direction == "U":
        makeWire(0, length, "y", 1)
    else:
        makeWire(0, length, "y", -1)

cur = [0, 0]

print("Creating Wire 2: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

for val in input[1]:
    direction = val[0:1]
    length = int(val[1:])

    if direction == "R":
        makeWire(1, length, "x", 1)
    elif direction == "L":
        makeWire(1, length, "x", -1)
    elif direction == "U":
        makeWire(1, length, "y", 1)
    else:
        makeWire(1, length, "y", -1)

print("Getting Intersection: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#intersection = intersection(wire)

# because calculating intersection was not efficient, i decided to reuse the value from previous run

intersection = [[403, 0], [610, 0], [681, 0], [854, 221], [681, 221], [604, 221], [170, 352], [170, 815], [170, 965], [297, 1026], [837, 712], [681, 629], [604, 629], [57, 629], [-132, 815], [-49, 1062], [-4, 1062], [57, 1062], [141, 1062], [297, 1062], [786, 712], [681, 545], [604, 545], [292, 815], [292, 965], [292, 1064], [292, 1091], [292, 1114], [292, 1277], [292, 1315], [258, 1454], [156, 1454], [68, 1114], [68, 1064], [68, 965], [68, 815], [68, 790], [297, 716], [315, 712], [57, 404], [-205, 404], [-488, 308], [-488, 0]]

print("List of intersection: ", intersection)

print("Calculating closest interesection: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

output[0] = closest(list(intersection))

output[1] = shortestpath(list(intersection))

print("Result: ", output)

print("Done: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))