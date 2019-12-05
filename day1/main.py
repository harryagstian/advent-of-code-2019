import os
import math

print('Hello, World!')

dirpath = os.getcwd()

with open(dirpath + '/day1/input.txt', 'r') as f:
    input = f.read().splitlines()

output = [0, 0]

def calculate0(val):
    # solution for part 1
    return (math.floor(val/3)-2)

def calculate1(val):
    # solution for part 2
    # val > 6 to prevent the fuel from getting negative value
    temp = 0
    while(val > 6):
        val = (math.floor(val/3)-2)
        temp += val 
    return temp

for val in input:
    output[0] += int(calculate0(int(val)))
    output[1] += int(calculate1(int(val)))

print(output)