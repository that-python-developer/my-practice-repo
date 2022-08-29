#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    from collections import deque
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_rotated = deque(alpha)
    alpha_rotated.rotate(-k)
    alpha_rotated = ''.join(list(alpha_rotated))
    alpha_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_caps_rotated = deque(alpha_caps)
    alpha_caps_rotated.rotate(-k)
    alpha_caps_rotated = ''.join(list(alpha_caps_rotated))

    final_string = ''
    for i in s:
        if i.islower() and i in alpha:
            final_string += alpha_rotated[alpha.index(i)]
        elif i.isupper() and i in alpha_caps:
            final_string += alpha_caps_rotated[alpha_caps.index(i)]
        else:
            final_string += i
    print(final_string)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # s = input()
    #
    # k = int(input().strip())

    s = "There's-a-starman-waiting-in-the-sky"
    k = 3
    s = 'www.abc.xy'
    k = 87
    result = caesarCipher(s, k)

    # fptr.write(result + '\n')
    #
    # fptr.close()
