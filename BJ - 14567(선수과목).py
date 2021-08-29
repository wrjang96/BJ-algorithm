import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
indegree = [0] * N
dp = [0] * N
graph = [[] for i in range(N)]
for i in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    graph[start].append(end)
    indegree[end] +=1

stack = deque()

for i in range(N):
    if indegree[i] == 0:
        stack.append(i)
        dp[i] += 1

while stack:
    temp = stack.popleft()
    for next_temp in graph[temp]:
        indegree[next_temp] -= 1
        dp[next_temp] = max(dp[temp] + 1, dp[next_temp])
        if indegree[next_temp] ==0:
            stack.append(next_temp)


print(*dp)