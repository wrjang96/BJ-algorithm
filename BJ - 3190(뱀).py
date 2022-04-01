N = int(input())
arr = [[0] * N for i in range(N)]
K = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(K):
    A,B = map(int, input().split())
    arr[A-1][B-1] = 1
L = int(input())
change = []
for i in range(L):
    A, B = map(str,input().split())
    change.append([int(A), B])

cnt = 0
flag = 0
queue = [[0,0]]
while 1:
    cnt += 1
    tx = queue[-1][0]
    ty = queue[-1][1]
    nx = tx + dx[flag]; ny = ty + dy[flag]
    if 0<= nx < N and 0<=ny <N and [nx,ny] not in queue:
        if arr[nx][ny] == 1:
            arr[nx][ny] = 0
            queue.append([nx,ny])
        else:
            queue.append([nx, ny])
            queue.pop(0)
    else:
        break
    if len(change) !=0 and change[0][0] == cnt:
        if change[0][1] == "L":
            flag -= 1
        else:
            flag += 1
        change.pop(0)
    flag = flag % 4
print(cnt)
