from sys import stdin
N = int(stdin.readline())
graph = list(map(int, stdin.readline().split()))
dp = [x for x in graph]
for i in range(N):
    for j in range(i):
        if graph[i] > graph[j]:
            dp[i]= max(dp[i], dp[j] + graph[i])
print(max(dp))