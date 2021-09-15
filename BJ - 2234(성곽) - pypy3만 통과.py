N, M = map(int, input().split())
graph = [[] for _ in range(M)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
visited = [[0] * N for i in range(M)]
breakable_wall = []

for i in range(M):
    temp = list(map(int, input().split()))
    for k in range(len(temp)):
        arr = [0] * 4
        for j in range(3,-1,-1):
            if temp[k] >= 2 ** j :
                temp[k] -= 2 ** j
                arr[j] += 1
        graph[i].append(arr)

queue = []
room_cnt = 0
diameter_cnt = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            room_cnt += 1
            queue.append([i,j])
            temp_cnt = 1
            while queue:
                x, y = queue.pop(0)
                visited[x][y] = 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and graph[x][y][k] == 0:
                        queue.append([nx,ny])
                        visited[nx][ny] = 1
                        temp_cnt += 1
                    if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and graph[x][y][k] == 1:
                        breakable_wall.append([x, y, k])
            if temp_cnt > diameter_cnt:
                diameter_cnt = temp_cnt
merge_room_cnt = 0

while breakable_wall:
    temp_merge_room_cnt = 0
    tx,ty,way = breakable_wall.pop(0)
    graph[tx][ty][way] = 0
    visited = [[0] * N for i in range(M)]
    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0:
                temp_merge_room_cnt = 1
                queue.append([i, j])
                while queue:
                    x, y = queue.pop(0)
                    visited[x][y] = 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and graph[x][y][k] == 0:
                            queue.append([nx, ny])
                            visited[nx][ny] = 1
                            temp_merge_room_cnt += 1
            if temp_merge_room_cnt > merge_room_cnt:
                merge_room_cnt = temp_merge_room_cnt
    graph[tx][ty][way] = 1

print(room_cnt)
print(diameter_cnt)
print(merge_room_cnt)