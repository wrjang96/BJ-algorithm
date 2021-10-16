import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[0] * M for i in range(N)]
answer = [[0] * M for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def search():
    visited = [[0] * M for i in range(N)]
    queue = deque([])
    queue.append([0,0])
    while queue:
        tx, ty = queue.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                queue.append([nx,ny])
                visited[nx][ny] = 1
            elif 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] !=0:
                graph[nx][ny] +=1
def erase():
    for i in range(N):
        for j in range(M):
            if 1<= graph[i][j] <= 2:
                graph[i][j] = 1
            elif graph[i][j] >= 3:
                graph[i][j] = 0
for _ in range(N):
    graph[_] = list(map(int,input().split()))

cnt = 0
while graph != answer:
    search()
    erase()
    cnt += 1
print(cnt)