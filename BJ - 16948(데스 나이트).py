from sys import stdin
N = int(stdin.readline())
graph = [[0] * N for i in range(N)]
visited = [[0] * N for i in range(N)]
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
r1,c1,r2,c2 = map(int,input().split())
def bfs(x,y,z,w):
    queue =[]
    queue.append([x,y,0])
    visited[x][y] =1
    while queue:
        px,py,tmpcnt = queue.pop(0)
        if px == z and py == w:
            return tmpcnt
            break
        for i in range(6):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                queue.append([nx, ny, tmpcnt+1])
                visited[nx][ny] = 1
    if visited[z][w] == 0:
        return -1

print(bfs(r1,c1,r2,c2))