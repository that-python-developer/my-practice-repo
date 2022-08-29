#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # for i in range(1, len(arr) - 1):
    #     if sum(arr[0:i]) == sum(arr[i+1:]):
    #         return 'YES'
    # return 'NO'
    for i in range(len(arr)):
        if sum(arr[0:i]) == sum(arr[i+1:]):
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # T = int(input().strip())
    #
    # for T_itr in range(T):
    #     n = int(input().strip())
    #
    #     arr = list(map(int, input().rstrip().split()))

    arr = [5, 6, 8, 11]
    result = balancedSums(arr)

    #     fptr.write(result + '\n')
    #
    # fptr.close()
