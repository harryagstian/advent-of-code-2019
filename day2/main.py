import os
from copy import deepcopy

print('Hello, World!')

dirpath = os.getcwd()

with open('input.txt', 'r') as f:
    input = [int(x) for x in f.readline().split(',')]

output = [0, 0]

def Intcode(list, pos):
    while True:
        op = list[pos]
        # print(pos, op)
        if op == 1:
            list[list[pos + 3]] = list[list[pos + 1]] + list[list[pos + 2]]
        elif op == 2:
            list[list[pos + 3]] = list[list[pos + 1]] * list[list[pos + 2]]
        elif op == 99:
            break
        else:
            break
        pos += 4
    return list[0]

# modify index 1 and 2 according to the puzzle

part1 = deepcopy(input)

part1[1] = 12
part1[2] = 2

output[0] = Intcode(part1, 0)

part2 = deepcopy(input)

found = False

# brute force solution for part 2 

for i in range(0,100):
    if found: 
        break
    for j in range(0,100):
        if found:  
            break
        part2 = deepcopy(input)
        part2[1] = i
        part2[2] = j
        if Intcode(part2, 0) == 19690720: 
            output[1] = (100 * i) + j
            found = True
            


print(output)