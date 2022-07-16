#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    print(sum(sorted_arr[0:-1]))
    print(sum(sorted_arr[1:]))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# input
# 1 2 3 4 5
