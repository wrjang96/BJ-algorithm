from collections import deque

N, M = map(int, input().split())
arr = [[] for i in range(N)]


cloud = deque()
cloud.append((N-1, 0))
cloud.append((N-1, 1))
cloud.append((N-2, 0))
cloud.append((N-2, 1))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(M):
    visited = [[0] * N for i in range(N)]
    dir, dis = map(int, input().split())
    # 1번 & 2번
    for j in range(len(cloud)):
        tx, ty = cloud.popleft()
        dis = dis % N
        nx = tx + (dx[dir - 1] * dis)
        ny = ty + (dy[dir - 1] * dis)
        if nx >= N:
            nx -= N
        if nx < 0:
            nx += N
        if ny >= N:
            ny -= N
        if ny < 0:
            ny += N
        cloud.append((nx, ny))
        arr[nx][ny] += 1
        visited[nx][ny] = 1


    for tx, ty in cloud:
        tcnt = 0
        for i in range(4):
            nx = tx + dx2[i]
            ny = ty + dy2[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > 0:
                    tcnt += 1
        arr[tx][ty] += tcnt

    cloud = deque([])

    # 5번 - visited 이용해서 확인해야 시간 복잡도가 줄어듬

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and visited[i][j] == 0:
                cloud.append((i,j))
                arr[i][j] -= 2

ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)