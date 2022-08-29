#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    # Refer to this logic https://medium.com/@mlgerardvla/hackerrank-sum-vs-xor-63e18dbd11cf
    # or this logic https://hackerranksolution.in/sumvsxoralgo/
    return 1 if n == 0 else pow(2, bin(n)[2:].count('0'))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    n = 1000000000000000
    result = sumXor(n)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
