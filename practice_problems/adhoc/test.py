# input_list = []
# for i in input():
#     input_list.append(i)
# print(input_list)

# input_list = {'Park': 'Richard', 'Steel': 'Andrea', 'Chang': 'Li'}
#
# temp = sorted(input_list.keys())
# for i in temp:
#     print(input_list.get(i))

# from itertools import combinations
# def minion_game(string):
#     kevin_score = stuart_score = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     all_combinations = [string[x:y].lower() for x, y in combinations(range(len(string) + 1), r=2)]
#     # all_combinations = [string[i: j].lower() for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
#     for i in all_combinations:
#         if i[0] in vowels:
#             kevin_score += 1
#         else:
#             stuart_score += 1
#     if kevin_score == stuart_score:
#         print('Draw')
#     elif kevin_score > stuart_score:
#         print('Kevin ', kevin_score)
#     elif stuart_score > kevin_score:
#         print('Stuart ', stuart_score)
#
# # your code goes here
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)



#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     # Write your code here
#     alice = bob = 0
#     for i in range(0, len(a)):
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1
#     return [alice, bob]
#
#
# if __name__ == '__main__':
#     a = [5, 6, 7]
#     b = [3, 6, 10]
#     result = compareTriplets(a, b)
#     print(result)


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         pass
#
# s = Solution
# s.firstBadVersion()
