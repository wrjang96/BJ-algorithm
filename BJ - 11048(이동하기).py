N, M = map(int, input().split())
arr = [[0] *M for i in range(N)]
dp = [[0] *M for i in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
dp[0][0] = arr[0][0]
for i in range(N):
    for j in range(M):
        if i == 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + arr[i][j]
print(dp[N-1][M-1])