import heapq
import sys

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dijkstra(graph, N):
    queue = []
    cost_sum = [[int(1e9)] * N for _ in range(N)]
    heapq.heappush(queue, [graph[0][0], 0,0])
    cost_sum[0][0] = 0
    answer = 0
    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == N-1 and y == N-1:
            answer = cost
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< N and 0<=ny < N:
                nCost = cost + graph[nx][ny]
                if nCost < cost_sum[nx][ny]:
                    cost_sum[nx][ny] = nCost
                    heapq.heappush(queue, [nCost,nx,ny])
    return answer

cnt = 1
while 1:
    N = int(input())
    if N == 0:
        break
    cost_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        cost_graph[i] = list(map(int,input().split()))
    print("Problem "+ str(cnt) + ": " + str(dijkstra(cost_graph, N)))
    cnt += 1
