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
    # am_pm = s[-2:]
    # if am_pm == 'PM':
    #     if s[0:2] == '12':
    #         return s[0:8]
    #     else:
    #         return '{}{}'.format(str(int(s[0:2])+12), s[2:8])
    # else:
    #     if s[0:2] == '12':
    #         return '00:{}'.format(s[2:8])
    #     else:
    #         return s[0:8]
    s = s.split(':')
    if s[-1][2:4] == 'AM':
        if s[0] == '12':
            return ':'.join(['00', s[1], s[-1][0:2]])
        else:
            return ':'.join([s[0], s[1], s[-1][0:2]])
    elif s[-1][2:4] == 'PM':
        if s[0] == '12':
            return ':'.join(['12', s[1], s[-1][0:2]])
        else:
            return ':'.join([str(int(s[0]) + 12), s[1], s[-1][0:2]])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
