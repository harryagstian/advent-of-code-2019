import os
import math

print('Hello, World!')

dirpath = os.getcwd()

with open(dirpath + '/day2/input.txt', 'r') as f:
    input = [int(x) for x in f.readline().split(',')]

output = [0, 0]

def Intcode(input):
    cur = 0
    while(input[cur] != 99):
        if input[cur] == 1:
            # addition
            input[input[cur+3]] = input[input[cur+1]] + input[input[cur+2]]
            cur += 4
        elif input[cur] == 2:
            # multiplication
            input[input[cur+3]] = input[input[cur+1]] * input[input[cur+2]]
            cur += 4
        else:
            break

    return input[0]

partOne = list(input)
partTwo = list(input)

# modify index 1 and 2 according to the puzzle

partOne[1] = 12
partOne[2] = 2

output[0] = Intcode(partOne)

# brute force solution for part 2 

for x in range(100):
    for y in range(100):
        partTwo = list(input)
        partTwo[1] = x
        partTwo[2] = y
        if Intcode(partTwo) == 19690720:
            output[1] = (100 * x) + y
            break

print(output)