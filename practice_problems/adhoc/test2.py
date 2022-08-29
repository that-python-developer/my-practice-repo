#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'strokesRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY picture as parameter.
#
def floodFill(i, j, m, n, prev, mat):
    if i >= m or i < 0 or j >= n or j < 0:
        return False
    if mat[i][j] == 0:
        return False
    if mat[i][j] == prev:
        mat[i][j] = 0
        if i < m-1:
            floodFill(i + 1, j, m, n, prev, mat)
        if i > 0:
            floodFill(i - 1, j, m, n, prev, mat)
        if j < n-1:
            floodFill(i, j + 1, m, n, prev, mat)
        if j > 0:
            floodFill(i, j - 1, m, n, prev, mat)
        return True


def strokesRequired(picture):
    # Write your code here
    if not picture:
        return 0
    mat = [[j for j in picture[i]] for i in range(len(picture))]

    m, n = len(picture), len(picture[0])
    res = 0
    for i in range(m):
        for j in range(n):
            r = floodFill(i, j, m, n, mat[i][j], mat)
            if r:
                res += 1
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # picture_count = int(input().strip())
    #
    # picture = []
    #
    # for _ in range(picture_count):
    #     picture_item = input()
    #     picture.append(picture_item)


    result = strokesRequired(["aaaba", "ababa", "aaaca"])
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
