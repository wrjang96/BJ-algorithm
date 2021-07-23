while(1):
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    arr_graph = [[[0 for i in range(C)] for j in range(R)]for k in range(L)]
    visited = [[[0 for i in range(C)] for j in range(R)]for k in range(L)]
    queue = []

    for i in range(L):
        for j in range(R):
             temp_str = str(input())
             for k in range(C):
                 arr_graph[i][j][k] = temp_str[k]
                 if arr_graph[i][j][k] == "S":
                     queue.append([i, j, k, 0])
                     visited[i][j][k] = 1
        temp = list(map(str, input().split()))
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    answer = 0
    while queue:
        x,y,z, cnt = queue.pop(0)
        if arr_graph[x][y][z] == "E":
            answer = cnt
            break
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<= nx < L and 0<= ny <R and 0<= nz <C and visited[nx][ny][nz] == 0 and arr_graph[nx][ny][nz] != "#":
                queue.append([nx,ny,nz,cnt + 1])
                visited[nx][ny][nz] = 1
    if answer == 0:
        print("Trapped!")
    else:
        print("Escaped in " + str(answer) + " minute(s).")

