#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    # 12:01:00PM
    # 0123456789
    am_or_pm = s[8:]
    format24 = s[0:8]
    hour = int(s[0:2])
    print(am_or_pm)
    print(format24)
    print(hour)
    
    if am_or_pm == 'PM' and hour < 12:
        hour += 12
        format24 = str(hour) + format24[2:8]
    elif am_or_pm == 'AM' and hour == 12:
        format24 = '00' + format24[2:8]
        
    return format24


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
