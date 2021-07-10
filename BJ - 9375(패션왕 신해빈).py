testcase_num = int(input())
while testcase_num:
    c_num = int(input())
    clothes_arr = {}
    while c_num:
        clothes, clothes_group = input().split()
        if (clothes_group in clothes_arr):
            clothes_arr[clothes_group] += 1
        else:
            clothes_arr[clothes_group] = 1
        c_num -= 1
    answer = 1
    for i in clothes_arr.keys():
        #print(clothes_arr[i])
        answer *= (clothes_arr[i] + 1)
    print(answer - 1)
    testcase_num -= 1
