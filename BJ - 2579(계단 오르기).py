N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())

# print(arr)
if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0] + arr[1])
else:
    dp = [0] * N
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = arr[2] + max(arr[0], arr[1])
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])
    print(dp[N - 1])

