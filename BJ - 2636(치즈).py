N,M = map(int,input().split())

graph = [[0 * M]for i in range(N)]
answer = [[0] * M for i in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))
queue =[]
erase =[]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cheese_num = []

def bfs(x, y):
    tmp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print(nx,ny)
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            queue.append([nx, ny])
            visited[nx][ny] = 1
            #print(nx, ny)
        elif 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            erase.append([nx, ny])
            visited[nx][ny] = 1
    tmp += len(erase)
    while(erase):
        graph[erase[0][0]][erase[0][1]] = 0
        erase.pop(0)
    return tmp
cnt =0
while(graph != answer):
    c_num = 0
    queue.append([0, 0])
    visited = [[0] * M for i in range(N)]
    visited[0][0] = 1
    while (queue):
        c_num += bfs(queue[0][0], queue[0][1])
        queue.pop(0)
    cnt+=1


print(cnt)
print(c_num)