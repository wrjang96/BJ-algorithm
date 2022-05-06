N, M = map(int, input().split())
arr = [[0] * N for i in range(M)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for i in range(M):
    tmp_str = input()
    for j in range(N):
        arr[i][j] = int(tmp_str[j])

visited = [[int(1e9)] * N for i in range(M)]

queue = [[0,0]]
visited[0][0] = 0
while queue:
    tx,ty = queue.pop(0)
    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]
        if 0 <= nx < M and 0 <=ny < N:
            if visited[nx][ny] > visited[tx][ty] + arr[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[tx][ty] + arr[nx][ny]

# for i in range(M):
#     print(visited[i])
print(visited[M-1][N-1])