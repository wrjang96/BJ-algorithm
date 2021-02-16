import sys
input = sys.stdin.readline
N= int(input())
graph = list(map(int,input().split()))
#dp = [0] * 100001
dp = [0] * (N)
dp[0] = graph[0]
for i in range(1,N):
    dp[i] = max(graph[i],graph[i]+ dp[i-1])

print(max(dp))