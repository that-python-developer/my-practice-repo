# # Example 1
# def cube(y):
#     return y * y * y
#
#
# lambda_cube = lambda y: y * y * y
#
# # using the normally defined function
# print(cube(5))
#
# # using the lambda function
# print(lambda_cube(5))

# # Example 2
# l = ['ab,c,tt', 'xcaidg,rt,yy']
# t = [lambda x=x: str(x).replace(',', '-') for x in l]
#
# for i in t:
#     print(i())

# # Example 3 - lambda function using if-else
# Max = lambda a, b: a if (a > b) else b
#
# print(Max(1, 2))

# # Example 4
# List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
#
# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)
#
# # Get the second largest element
# secondLargest = lambda l, f: [y[len(y) - 2] for y in f(l)]
# res = secondLargest(List, sortList)
#
# print(res)

# # Example 5 - filter() with lambda()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# final_list = list(filter(lambda x: (x % 2 != 0), li))
#
# print(final_list)

# # Example 6 - map() with lambda()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# final_list = list(map(lambda x: x * 2, li))
# print(final_list)

# # Example 7 - reduce() with lambda()
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)
