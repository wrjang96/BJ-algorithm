import sys
from collections import deque
input = sys.stdin.readline

testcase = int(input())
for i in range(testcase):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    indegree = [0] * N
    dp = [0] * N
    graph = [[] for i in range(N)]
    while K:
        start, end = map(int, input().split())
        start -= 1
        end -= 1
        graph[start].append(end)
        indegree[end] += 1
        K -= 1
    W = int(input())
    W -= 1
    stack = deque()
    for j in range(N):
        if indegree[j] == 0:
            stack.append(j)
            dp[j] = time[j]
    while stack:
        temp_s = stack.popleft()
        for temp_n in graph[temp_s]:
            indegree[temp_n] -= 1
            dp[temp_n] = max(dp[temp_s] + time[temp_n], dp[temp_n])
            if indegree[temp_n] ==0:
                stack.append(temp_n)
    print(dp[W])