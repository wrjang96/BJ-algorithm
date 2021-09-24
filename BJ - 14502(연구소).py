from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
import copy
N,M = map(int, input().split())
graph = [[0] * M for _ in range(N)]

blank = []
starting_point = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
answer_cnt = 0
for i in range(N):
    graph[i] = list(map(int, input().split()))
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            blank.append([i, j])
        elif graph[i][j] == 2:
            starting_point.append([i, j])

temp = list(combinations(blank, 3))

for i in range(len(temp)):
    temp_graph = copy.deepcopy(graph)
    for j in range(len(temp[i])):
        temp_graph[temp[i][j][0]][temp[i][j][1]] = 1
    queue = copy.deepcopy(starting_point)
    queue = deque(queue)
    visited = [[0] * M for _ in range(N)]
    while queue:
        # print(queue)
        x, y = queue.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < N and 0<= ny <M and visited[nx][ny] == 0 and temp_graph[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                temp_graph[nx][ny] = 2
    cnt = 0
    for i in range(N):
        cnt += temp_graph[i].count(0)
    if answer_cnt < cnt:
        answer_cnt = cnt
print(answer_cnt)