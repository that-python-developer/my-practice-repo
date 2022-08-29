with open("odd_test_input.txt", "r+") as f:
    # t = f.read().split('\n')
    # for x in t:
    #     try:
    #         if int(x) % 2 != 0:
    #             print(int(x))
    #     except Exception as e:
    #         pass
    j = 0
    output_list = []
    for x in f:
        try:
            if int(x) % 2 != 0:
                print(int(x))
                output_list.append(x)
                j += 1
            if j >= 4:
                break
        except Exception as e:
            pass

with open("odd_test_output.txt", "w") as write_file:
    for x in output_list:
        write_file.write(x)