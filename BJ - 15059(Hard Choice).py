having = list(map(int, input().split()))
wanted = list(map(int, input().split()))

cnt = 0
for i in range(3):
    if wanted[i] > having[i]:
        cnt += wanted[i] - having[i]
print(cnt)
