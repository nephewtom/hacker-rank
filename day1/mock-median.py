#!/bin/python3

import math


def median(arr):
    size = len(arr)
    arr.sort()
    index = math.floor(size / 2)
    return arr[index]


if __name__ == '__main__':
    a = [2, 1, 5, 3, 4]
    result = median(a)
    print(result)
