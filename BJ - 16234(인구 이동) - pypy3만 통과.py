N, L, R = map(int, input().split())
arr = [[0] * N for i in range(N)]
visited = [[0] * N for i in range(N)]

dx =[1,-1,0,0]
dy =[0,0,1,-1]

for i in range(N):
    arr[i] = list(map(int, input().split()))

def bfs(x,y,arr):
    queue = []
    global tqueue
    global visited
    queue.append([x, y])
    tqueue.append([x, y])
    cnt = 1
    sum = arr[x][y]
    while queue:
        x,y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                dif = abs(arr[nx][ny] - arr[x][y])
                if L <= dif and dif <= R:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append([nx,ny])
                        tqueue.append([nx, ny])
                        cnt += 1
                        sum += arr[nx][ny]
    return sum, cnt

ans_cnt = 0
while 1:
    return_flag = True
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                tqueue = []
                tsum, tcnt = bfs(i, j, arr)
                if len(tqueue) > 1:
                    while tqueue:
                        x, y = tqueue.pop()
                        arr[x][y] = tsum // tcnt
                    return_flag = False

    if return_flag == True:
        break
    ans_cnt += 1
print(ans_cnt)
