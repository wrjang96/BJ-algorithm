import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[int(1e9)] * N  for _ in range(N)]
for i in range(M):
    heavy_s, light_s = map(int, input().split())
    heavy_s -= 1
    light_s -= 1
    graph[heavy_s][light_s] = 1
    graph[light_s][heavy_s] = 1

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
arr= [i for i in range(N)]
answer = list(combinations(arr, 2))
answer = answer[::-1]
answer_arr = []
for k in range(len(answer)):
    answer_sum = 0
    for i in range(N):
        answer_sum += (min(graph[i][answer[k][0]],graph[i][answer[k][1]]) * 2)
    answer_arr.append([answer_sum,answer[k][0] + 1,answer[k][1] + 1])
answer_arr.sort()
print(answer_arr[0][1],answer_arr[0][2],answer_arr[0][0])
