import os
from copy import deepcopy

print('Hello, World!')

dirpath = os.getcwd()

with open('input', 'r') as f:
    input = [int(x) for x in f.readline().split(',')]

output = [0, 0]

def parseIntCode(v):
    v = str(v)
    opcode = int(v[-2:])
    v = v[::-1]
    m1 = int(v[2:3]) if v[2:3] != '' else None
    m2 = int(v[3:4]) if v[3:4] != '' else None
    m3 = int(v[4:5]) if v[4:5] != '' else None
    
    return opcode, m1, m2, m3

def Intcode(arr, pos):
    while True:
        opcode = arr[pos]
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
            usrInput = 1
            arr[p1] = int(usrInput)
            nextCode = 2
        elif opcode == 4:
            print(arr[p1])
            nextCode = 2
        elif opcode == 99:
            break
        else:
            break
        pos += nextCode
    return arr[0]

#part 1 

Intcode(input, 0)

