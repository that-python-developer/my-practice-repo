#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
    # Write your code here
    t = n
    turn = 'Louise'
    while t > 1:
        if (t & (t-1) == 0) and n != 0:
            t = t / 2
        else:
            t
        if t == 1:
            return

    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # t = int(input().strip())
    #
    # for t_itr in range(t):
    #     n = int(input().strip())

    n = 132
    result = counterGame(n)

    #     fptr.write(result + '\n')
    #
    # fptr.close()
