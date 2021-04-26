dp=[[0 for j in range(31)] for i in range(31)]
for i in range(1,31):
    dp[0][i] = 1

dp[1][1] = 1
for i in range(1,31):
    for j in range(1,i+1):
        dp[j][i] = dp[j][i-1] + dp[j-1][i]

while(1):
    N = int(input())
    if N ==0:
        break
    else:
        print(dp[N][N])
