from sys import stdin
N = int(stdin.readline())
graph = list(map(int, stdin.readline().split()))
dp = [1 for i in range(N)]
#print(dp)
for i in range(N):
    for j in range(i):
        if graph[i] > graph[j]:
            dp[i]= max(dp[i], dp[j] + 1)
print(max(dp))