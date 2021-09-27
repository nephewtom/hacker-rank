#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    count_map = {}
    for i in a:
        if i in count_map:
            count_map[i] = count_map[i]+1
        else:
            count_map[i] = 1
    
    for m in count_map:
        print(f"{m},{count_map[m]}", end='|')    
        if count_map[m] == 1:
            lonely = m
            break
    return lonely
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
