def move(nx,ny, flag):
    global queue
    global N
    global answer
    global arr
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    tmp = 0
    sand = arr[nx][ny]
    for j in range(len(queue[flag])):
        if 0 <= nx + queue[flag][j][0] < N and 0 <= ny + queue[flag][j][1] < N:
            arr[nx + queue[flag][j][0]][ny + queue[flag][j][1]] += int(sand * queue[flag][j][2])
            tmp += int(sand * queue[flag][j][2])
        else:
            answer += int(arr[nx][ny] * queue[flag][j][2])
            tmp += int(sand * queue[flag][j][2])

    if 0 <= nx + dx[flag] < N and 0 <= ny + dy[flag] <N:
        arr[nx + dx[flag]][ny + dy[flag]] += (sand - tmp)
    else:
        answer += (sand- tmp)

answer = 0
N = int(input())
arr = [[0]* N for i in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
sx = N//2
sy = N//2
dx = [0,1,0,-1]
dy = [-1,0,1,0]

flag = 0
queue = [[[-1,-1,0.1],[1,-1,0.1],[-1,0,0.07],[1,0,0.07],[0,-2,0.05],[2,0,0.02],[-2,0,0.02],[-1,1,0.01],[1,1,0.01]],
         [[1,1,0.1],[1,-1,0.1],[0,-1,0.07],[0,1,0.07],[2,0,0.05],[0,-2,0.02],[0,2,0.02],[-1,1,0.01],[-1,-1,0.01]],
         [[-1,1,0.1],[1,1,0.1],[-1,0,0.07],[1,0,0.07],[0,2,0.05],[2,0,0.02],[-2,0,0.02],[-1,-1,0.01],[1,-1,0.01]],
         [[-1,1,0.1],[-1,-1,0.1],[0,-1,0.07],[0,1,0.07],[-2,0,0.05],[0,-2,0.02],[0,2,0.02],[1,1,0.01],[1,-1,0.01]]
         ]



for i in range(1, N-1):
    for j in range(i):
        nx = sx + dx[flag % 4]
        ny = sy + dy[flag % 4]
        move(nx,ny, flag % 4)
        sx = nx
        sy = ny
    flag += 1

    for j in range(i):
        nx = sx + dx[flag % 4]
        ny = sy + dy[flag % 4]
        move(nx,ny, flag % 4)
        sx = nx
        sy = ny
    flag += 1

for i in range(N-1,N):
    for j in range(i):
        nx = sx + dx[flag % 4]
        ny = sy + dy[flag % 4]
        move(nx,ny, flag % 4)
        sx = nx
        sy = ny
    flag += 1
    for j in range(i):
        nx = sx + dx[flag % 4]
        ny = sy + dy[flag % 4]
        move(nx,ny, flag % 4)
        sx = nx
        sy = ny
    flag += 1
    for j in range(i):
        nx = sx + dx[flag % 4]
        ny = sy + dy[flag % 4]
        move(nx,ny, flag % 4)
        sx = nx
        sy = ny
    flag += 1
print(answer)