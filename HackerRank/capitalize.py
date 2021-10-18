# capitalize 1st charecter of each word, only if it is a char. 
# if 1st char is a number.. that should be skipped


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        print(s)
        s = s.replace(x, x.capitalize())
    return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
