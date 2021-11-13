import sys; input = sys.stdin.readline
from itertools import combinations

N = int(input())
cost = [[0] * N for i in range(N)]
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
for i in range(N):
    cost[i] = list(map(int, input().split()))
arr = []
answer = 1E9
for i in range(1, N-1):
    for j in range(1, N-1):
        arr.append([i,j])

candidates = list(combinations(arr,3))
for candidate in candidates:
    visited = [[0] * N for i in range(N)]
    answer_cost = 0
    for i in range(5):
        visited[candidate[0][0] + dx[i]][candidate[0][1] + dy[i]] += 1
        visited[candidate[1][0] + dx[i]][candidate[1][1] + dy[i]] += 1
        visited[candidate[2][0] + dx[i]][candidate[2][1] + dy[i]] += 1
        answer_cost += cost[candidate[0][0] + dx[i]][candidate[0][1] + dy[i]]
        answer_cost += cost[candidate[1][0] + dx[i]][candidate[1][1] + dy[i]]
        answer_cost += cost[candidate[2][0] + dx[i]][candidate[2][1] + dy[i]]
    max_num = 0
    for i in range(N):
        max_num = max(max_num, max(visited[i]))
    if max_num == 1:
        answer = min(answer, answer_cost )

print(answer)

