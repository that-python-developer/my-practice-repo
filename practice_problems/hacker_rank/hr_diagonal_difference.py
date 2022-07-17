#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    left_diagonal = right_diagonal = 0
    for i, outer_element in enumerate(arr):
        for j, inner_element in enumerate(outer_element):
            if i == j:
                left_diagonal += inner_element
            if i + j == len(outer_element) - 1:
                right_diagonal += inner_element
    print(abs(left_diagonal - right_diagonal))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
