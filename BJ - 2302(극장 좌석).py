N = int(input())
M = int(input())
arr = [0] * (N+1)
dp = [0] * 41

def numcnt():
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(2, 41):
        dp[i] = dp[i-1] + dp[i-2]

for i in range(M):
    tmp = int(input())
    arr[tmp] = 1
numcnt()
# print(dp)

ans = 1
cnt = 0
for i in range(1, N + 1):
    if arr[i] == 1:
        ans *= dp[cnt]
        cnt = 0
    else:
        cnt += 1
if cnt !=0:
    ans *= dp[cnt]

print(ans)