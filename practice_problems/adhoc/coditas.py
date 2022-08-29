# def reverse(s):
#     return ''.join([s[i] for i in range(len(s) - 1, -1, -1) if s != ''])
#
# def sum_of_top_two(arr):
#     max_no = second_max = 0
#     for i in range(len(arr)):
#         if arr[i] > max_no:
#             max_no = arr[i]
#         if arr[i] > second_max and max_no != arr[i]:
#             second_max = max_no
#     print(max_no, second_max)
#
#
# if __name__ == '__main__':
#     s = 'richard'
#     reversed_string = reverse(s)
#     print(reversed_string)
#     arr = [3, 6, 1, 4, 5]
#     sum_of_top_two(arr)
#

List = [[4, 3, 2], [1, 4, 16, 64], [3, 6, 9, 12]]

SortList = lambda x: (sorted(i) for i in x)

t = lambda l, f: [i[len(i) - 2] for i in f(l)]
print(list(t(List, SortList)))