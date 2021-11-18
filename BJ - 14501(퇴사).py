import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)
time = [0] * N
profit = [0] * N

for i in range(N):
    tmp_time, tmp_profit = map(int, input().split())
    time[i] = tmp_time
    profit[i] = tmp_profit

for i in range(N-1, -1, -1):
    if time[i] + i <= N:
        dp[i] = max(profit[i] + dp[time[i] + i],dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])

















# for i in range(N):
#     if dp[i] < dp[i-1]:
#         dp[i] = dp[i-1]
#     if i + time[i] >= N:
#         continue
#     if dp[i + time[i]] < dp[i] + profit[i]:
#         dp[i + time[i]] = dp[i] + profit[i]
#     print(dp)
# print(dp[N - 1])