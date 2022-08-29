#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    from collections import Counter
    total_pairs = 0
    for k, v in Counter(ar).items():
        print(k, v)
        total_pairs += v // 2
    print(total_pairs)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # ar = list(map(int, input().rstrip().split()))

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    # ar = [1, 2, 1, 2, 1, 3, 2]
    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
