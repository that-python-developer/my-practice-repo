#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    binary = bin(n)
    result = ''.join(['1' if x == '0' else '0' for x in str(binary)[2:].zfill(32)])
    return int(result, 2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # q = int(input().strip())
    #
    # for q_itr in range(q):
    #     n = int(input().strip())

    n = 4
    result = flippingBits(n)

    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
