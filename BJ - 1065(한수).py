X = int(input())
ans = 0
for i in range(1, X+1):
    if 1 <= i <= 99:
        ans +=1
    else:
        i = str(i)
        ans_flag = True
        flag = int(i[0]) - int(i[1])
        for k in range(1, len(i)-1):
            tmp = int(i[k]) - int(i[k+1])
            if tmp != flag:
                ans_flag = False
                break
        if ans_flag == True:
            ans +=1
print(ans)