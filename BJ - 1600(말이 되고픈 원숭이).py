from sys import stdin
K = int(stdin.readline())
W,H = map(int,stdin.readline().split())
graph = [[0] * (W) for i in range(H)]
visited = set()
queue = []
for i in range(H):
    graph[i] = list(map(int,stdin.readline().split()))
queue.append([0,0,0,0])
visited.add((0,0,0))
result = -1
dx = [-1,1,0,0]
dy = [0,0,1,-1]
hx = [2,2,-2,-2,1,1,-1,-1]
hy = [1,-1,1,-1,2,-2,2,-2]
while queue:
    x,y,cnt,step = queue.pop(0)
    if x == H-1 and y == W -1:
        result = step
        break
    for i in range(0,4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != 1 and (nx, ny, cnt) not in visited:
            queue.append([nx, ny, cnt, step + 1])
            visited.add((nx, ny, cnt))
    for i in range(0,8):
        mx = x + hx[i]
        my = y + hy[i]
        if 0 <= mx < H and 0 <= my < W and graph[mx][my] != 1 and cnt < K and (mx, my, cnt + 1) not in visited:
            queue.append([mx, my, cnt + 1, step + 1])
            visited.add((mx, my, cnt + 1))
print(result)
