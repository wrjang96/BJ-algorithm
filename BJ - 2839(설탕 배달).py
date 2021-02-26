N = int (input());
cnt = - 1
if cnt % 5 == 0:
    cnt = N // 5
else:
    temp = N % 5
    while (temp <= N):
        if temp % 3 == 0:
            cnt = (N - temp) // 5 + temp // 3
            break
        else:
            temp += 5
print(cnt)
