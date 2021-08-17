import sys
input = sys.stdin.readline
T = int(input())
while T:
    N = int(input())
    arr = [[0] * N for i in range(2)]
    dp = [[0] * N for i in range(2)]
    for i in range(2):
        arr[i] = list(map(int, input().split()))
    if N == 1: # 예외 처리 안하면 인덱스 에러 뜸
        print(max(arr[0][0], arr[1][0]))
    else:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]
        for i in range(2, N):
            dp[0][i] = max(arr[0][i] + dp[1][i - 1], arr[0][i] + dp[0][i - 2], arr[0][i] + dp[1][i - 2])
            dp[1][i] = max(arr[1][i] + dp[0][i - 1], arr[1][i] + dp[1][i - 2], arr[1][i] + dp[0][i - 2])
        print(max(dp[0][N - 1], dp[1][N - 1]))
    T -= 1