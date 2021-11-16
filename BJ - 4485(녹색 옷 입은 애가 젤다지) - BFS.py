import heapq
import sys
from collections import deque

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(graph, N):
    queue = deque([[0,0]])
    cost_sum = [[int(1e9)] * N for _ in range(N)]
    cost_sum[0][0] = graph[0][0]
    while queue:
        tx, ty = queue.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0<=nx <N and 0<=ny <N and cost_sum[nx][ny] > cost_sum[tx][ty] + graph[nx][ny]:
                queue.append([nx,ny])
                cost_sum[nx][ny] = cost_sum[tx][ty] + graph[nx][ny]
    return cost_sum[N-1][N-1]

cnt = 1
while 1:
    N = int(input())
    if N == 0:
        break
    cost_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        cost_graph[i] = list(map(int,input().split()))
    print("Problem "+ str(cnt) + ": " + str(bfs(cost_graph, N)))
    cnt += 1
