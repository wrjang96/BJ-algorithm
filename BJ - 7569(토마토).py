import sys
from collections import deque
input = sys.stdin.readline

dz = [0,0,0,0,1,-1]
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
M, N, H = map(int, input().split())
arr = [[[0] * M for i in range(N)] for i in range(H)]
visited = [[[0] * M for i in range(N)] for i in range(H)]
tomato = deque()

def check(arr):
    flag = True
    cnt = 0
    maxnum = -2
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0:
                    flag = False
                if arr[k][i][j] > maxnum:
                    maxnum = arr[k][i][j]
    return flag, maxnum

def ripe(arr, tomato):
    temp = []
    while tomato:
        tz,tx,ty = tomato.popleft()
        for i in range(6):
            nz = tz + dz[i]
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nz <H and 0 <= nx < N and 0<= ny <M and visited[nz][nx][ny] == 0 and arr[nz][nx][ny] == 0:
                visited[nz][nx][ny] = 1
                arr[nz][nx][ny] = arr[tz][tx][ty] + 1
                tomato.append([nz,nx, ny])



for k in range(H):
    for i in range(N):
        arr[k][i] = list(map(int, input().split()))
        for j in range(M):
            if arr[k][i][j] == 1:
                tomato.append([k,i,j])
                visited[k][i][j] = 1
ripe(arr, tomato)
flag, cnt = check(arr)
# print(arr)
if flag:
    print(cnt-1)
else:
    print(-1)
