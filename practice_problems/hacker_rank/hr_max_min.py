#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    min_unfairness = float('inf')
    arr = sorted(arr)
    for i in range(len(arr) - k + 1):
        if (arr[i+k-1] - arr[i]) < min_unfairness:
            min_unfairness = arr[i+k-1] - arr[i]
    print(min_unfairness)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # k = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(n):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)
    k = 2
    arr = [1, 4, 7, 2]
    k = 4
    arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
    k = 3
    arr = [100, 200, 300, 350, 400, 401, 402]
    result = maxMin(k, arr)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
