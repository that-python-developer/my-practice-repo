#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr_len = len(arr)
    return sorted(arr)[int(arr_len/2):int(arr_len/2)+1][0]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))

    arr = [0,1,2,4,6,5,3]
    result = findMedian(arr)
    print(result)


    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
