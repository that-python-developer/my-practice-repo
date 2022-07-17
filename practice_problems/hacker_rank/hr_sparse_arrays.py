#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    result_list = [0] * len(queries)
    for i in range(0, len(queries)):
        for s in strings:
            if queries[i] == s:
                result_list[i] += 1
    return result_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # strings_count = int(input().strip())
    #
    # strings = []
    #
    # for _ in range(strings_count):
    #     strings_item = input()
    #     strings.append(strings_item)
    #
    # queries_count = int(input().strip())
    #
    # queries = []
    #
    # for _ in range(queries_count):
    #     queries_item = input()
    #     queries.append(queries_item)

    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']

    res = matchingStrings(strings, queries)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
