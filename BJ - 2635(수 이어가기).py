N = int(input())
answercnt = 0
answer_list = []
for i in range(N, 0, -1):
    tmp_list = []
    tmp_list.append(N)
    tmp1 = N
    tmp2 = i
    cnt = 2
    while 1:
        if tmp1 - tmp2 < 0:
            if answercnt < cnt:
                answercnt = cnt
                tmp_list.append(tmp2)
                answer_list = tmp_list
            break
        else:
            tmp_list.append(tmp2)
            swaptmp = tmp1 - tmp2
            tmp1 = tmp2
            tmp2 = swaptmp
            cnt += 1
print(answercnt)
print(*answer_list)