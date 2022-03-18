level = int(input())
ans = int(input())

max_num = level //2
arr = [[0] * (max_num *2 + 1) for i in range(max_num *2 + 1)]
arr[max_num][max_num] = 1
tx = max_num
ty = max_num

dx = [-1,0,1,0,-1]
dy = [0,1,0,-1,0]
for i in range(1, max_num + 1):
    nx = dx[0] + tx
    ny = dy[0] + ty
    arr[nx][ny] = arr[tx][ty] + 1
    tx = nx; ty = ny;
    for j in range(i * 2 - 1):
        nx = tx + dx[1]
        ny = ty + dy[1]
        arr[nx][ny] = arr[tx][ty] + 1
        tx = nx; ty = ny;
    for j in range(i * 2):
        nx = tx + dx[2]
        ny = ty + dy[2]
        arr[nx][ny] = arr[tx][ty] + 1
        tx = nx; ty = ny;
    for j in range(i * 2):
        nx = tx + dx[3]
        ny = ty + dy[3]
        arr[nx][ny] = arr[tx][ty] + 1
        tx = nx; ty = ny;
    for j in range(i * 2):
        nx = tx + dx[4]
        ny = ty + dy[4]
        arr[nx][ny] = arr[tx][ty] + 1
        tx = nx; ty = ny;

ansx = 0
ansy = 0
for i in range(level):
    for j in range(level):
        print(arr[i][j], end=" ")
        if arr[i][j] == ans:
            ansx = i
            ansy = j
    print()

print(ansx + 1,ansy + 1)

