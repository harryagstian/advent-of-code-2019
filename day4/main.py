import os
from datetime import datetime
import copy

print('Hello, World!')

output = [0, 0]

# 1. must have double in sequence
# 2. never decrease

def validate(valueInt):
    first = False
    second = True
    
    valueStr = str(valueInt)

    if second == True:
        # check second rule
        for i in range(len(valueStr)-1):
            if valueStr[i] > valueStr[i+1]:
                second = False
                break

    if first == False and second == True:
        # check first rule
        for i in range(len(valueStr)-1):
            if valueStr[i] == valueStr [i+1]:
                # 2nd part require the pair not be a part of bigger sets
                if valueStr.count(valueStr[i]) == 2:
                    first = True
                    break

    if first == True and second == True:
        return True
    else:
        return False

# input here
start = 235741
current = start
end = 706948

result = []

while current < end:
    if validate(current):
        result.append(current)
    current += 1


output[0] = len(result)

print("Result: ", output)