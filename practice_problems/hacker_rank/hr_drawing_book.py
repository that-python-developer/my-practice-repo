#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here

    pages_from_start = math.ceil((p - 1) / 2)
    pages_from_end = math.ceil((n - p) / 2) if n % 2 == 0 else math.floor((n - p) / 2)
    print(min(pages_from_start, pages_from_end))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # p = int(input().strip())

    n = 5
    p = 4
    result = pageCount(n, p)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
