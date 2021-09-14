#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    zeroes = 0
    positives = 0
    negatives = 0
    for x in arr:
        if x > 100 or x < -100:
            print("Elements can not be outside [-100, 100] range")
            return
        if x == 0:
            zeroes += 1
        elif x > 0:
            positives += 1
        else:
            negatives += 1

    size = len(arr)
    print("%.6f\n%.6f\n%.6f\n" % (positives/size, negatives/size, zeroes/size))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    if len(arr) == 0 or len(arr) > 100:
        print("Array can not be greater than 100 elements")
    else:     
        plusMinus(arr)
