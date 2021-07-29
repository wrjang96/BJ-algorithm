N = int(input())
test_class =list(map(int,input().split()))
B,C = map(int,input().split())

cnt = N

for i in range(N):
    test_class[i]-= B
    if test_class[i] < 0:
        test_class[i] = 0

if sum(test_class) != 0:
    for temp_num in test_class:
        if temp_num > 0:
            if temp_num % C == 0:
                cnt += temp_num // C
            else:
                cnt += (temp_num // C + 1)
print(cnt)