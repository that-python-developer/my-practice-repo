def dummy_func(input_list):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i][j] == input_list[j][i]:
                continue
            else:
                return 'Error'
    return 'Success'


if __name__ == '__main__':
    input_list = ['BALLS', 'AREAK', 'LEADS', 'LADYS', 'SKSST']
    print(input_list)
    result = dummy_func(input_list)
    print(result)

#     0   1   2   3   4
# 0   B   A   L   L   S
# 1   A   R   E   A   K
# 2   L   E   A   D   S
# 3   L   A   D   Y   S
# 4   S   K   S   S   T
