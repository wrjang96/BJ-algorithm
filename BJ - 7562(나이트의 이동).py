from collections import deque


dx= [2,2,-2,-2,1,1,-1,-1]
dy= [1,-1,1,-1,2,-2,2,-2]


def bfs():
    queue = deque()
    queue.append([fromx,fromy])
    visited[fromx][fromy] =1
    while queue:
        tempx,tempy= queue.popleft()
        if tempx == tox and tempy == toy:
            return visited[tox][toy]
        for i in range(0,8,1):
            nx = tempx + dx[i]
            ny = tempy + dy[i]
            if 0<=nx<I and 0<=ny<I:
                if visited[nx][ny]==0:
                    queue.append([nx,ny])
                    visited[nx][ny] = visited[tempx][tempy] +1
        
testcase = int(input())
while testcase:
    I = int(input())
    visited = [[0] * (I) for i in range(I)]
    fromx,fromy = map(int,input().split())
    tox,toy = map(int,input().split())
    ans = bfs()
    print(ans-1)
    testcase-=1
        
