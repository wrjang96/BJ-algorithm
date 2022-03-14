testcase = int(input())
while testcase:
    temp = input()
    flag = False
    if len(temp) == 7:
        tmp = []
        for i in range(7):
            tmp.append(temp[i])
        tmp = set(tmp)
        if len(set(tmp)) == 2:
            one = tmp.pop()
            two = tmp.pop()
            com_a = one + one + two + two + one + two + two
            com_b = two + two + one + one + two + one + one
            if temp == com_a or temp == com_b:
                flag = True
    if flag == True:
        print(1)
    else:
        print(0)
    testcase -= 1