import sys
from copy import deepcopy
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[0] * M for _ in range(N)]
meltall = [[0] * M for _ in range(N)]
dx =[0,0,1,-1]
dy =[1,-1,0,0]

def count(x,y):
    queue =[]
    queue.append([x,y])
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] > 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])


def melt(graph):
    temp = deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if temp[i][j] >0:
                meltcnt =0
                for k in range(4):
                    nnx = i + dx[k]
                    nny = j + dy[k]
                    if temp[nnx][nny]<=0:
                        meltcnt +=1
                graph[i][j] -= meltcnt
                if graph[i][j] <0:
                    graph[i][j] =0

for i in range(N):
    graph[i] = list(map(int,input().split()))

cnt =0
while (1):
    cnt +=1
    melt(graph)
    visited = [[0] * M for _ in range(N)]
    island = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and visited[i][j] == 0:
                island += 1
                count(i, j)
    if graph == meltall:
        print(0)
        break
    if island > 1:
        print(cnt)
        break