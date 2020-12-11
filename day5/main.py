import os
from copy import deepcopy

print('Hello, World!')

dirpath = os.getcwd()

with open('input', 'r') as f:
    input = [int(x) for x in f.readline().split(',')]

def parseIntCode(v):
    v = str(v)
    opcode = int(v[-2:])
    v = v[::-1]
    m1 = int(v[2:3]) if v[2:3] != '' else None
    m2 = int(v[3:4]) if v[3:4] != '' else None
    m3 = int(v[4:5]) if v[4:5] != '' else None
    
    return opcode, m1, m2, m3

def Intcode(arr, pos, usrInput):
    while True:
        # print(pos, arr[pos], len(arr))
        opcode = arr[pos]
        if opcode == 99:
            break
        
        p1 = arr[pos + 1]
        p2 = arr[pos + 2]
        p3 = arr[pos + 3]
        nextCode = 4

        if arr[pos] > 100:
            opcode, m1, m2, m3 = parseIntCode(arr[pos])

            if m1 == 1:
                p1 = pos + 1
            if m2 == 1:
                p2 = pos + 2 
            if m3 == 1:
                p3 = pos + 3

        # print(pos, opcode, arr[pos], nextCode)
        if opcode == 1:
            arr[p3] = arr[p1] + arr[p2]
        elif opcode == 2:
            arr[p3] = arr[p1] * arr[p2]
        elif opcode == 3:
            arr[p1] = usrInput
            nextCode = 2
        elif opcode == 4:
            print(arr[p1])
            nextCode = 2
        elif opcode == 5:
            nextCode = 3
            if arr[p1] != 0:
                nextCode = arr[p2] - pos
        elif opcode == 6:
            nextCode = 3
            if arr[p1] == 0:
                nextCode = arr[p2] - pos
        elif opcode == 7:
            val = 0
            if arr[p1] < arr[p2]:
                val = 1
            arr[p3] = val
        elif opcode == 8:
            val = 0
            if arr[p1] == arr[p2]:
                val = 1
            arr[p3] = val
        pos += nextCode
    return arr[0]

#part 1 

print('Part 1' )

Intcode(input, 0, 1)

print('Part 2')

Intcode(input, 0, 5)

