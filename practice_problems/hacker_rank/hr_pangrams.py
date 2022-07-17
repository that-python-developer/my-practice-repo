#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabets = sorted(set('abcdefghijklmnopqrstuvwxyz'))
    s = sorted(set(s.lower().replace(' ', '')))
    return 'pangram' if alphabets == s else 'not pangram'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()

    s = 'We promptly judged antique ivory buckles for the next prize'
    result = pangrams(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
