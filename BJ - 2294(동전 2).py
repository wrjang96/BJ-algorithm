# import heapq
N, K = map(int, input().split())
dp = [int(1e9)] * (K+1)
coin = []
coin.sort()
for i in range(N):
    temp = int(input())
    for j in range(temp, K+1):
        dp[j] = min(dp[j], dp[j - temp] + 1)
print(dp)
