#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'commonPrefix' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.
#

def commonPrefix(inputs):
    print(inputs)
    prefixes_array_total = []
    for string in inputs:
        suffixes = []
        score = 0
        for i in range(len(string)):
            suffixes.append(string[i:])
        
        for suffix1 in suffixes:
            length = len(suffix1)
            for i in range(length,0,-1):
                if suffix1[0:i] == string[0:i]:
                    score += len(suffix1[0:i])
                    break
        
        
        del suffixes
        prefixes_array_total.append(score)
    
    return(prefixes_array_total)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputs_count = int(input().strip())

    inputs = []

    for _ in range(inputs_count):
        inputs_item = input()
        inputs.append(inputs_item)

    result = commonPrefix(inputs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
