import sys
input = sys.stdin.readline
N = int(input())
graph = list(map(int, input().split()))
dp = [1 for i in range(N)]
for i in range (len(graph)):
    for j in range (i):
        if graph[j] >graph[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))