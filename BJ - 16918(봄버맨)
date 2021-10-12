from collections import deque
R, C, N = map(int, input().split())
graph = [[0] * C for i in range(R)]
next_bomb = deque([])
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def set_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "O":
                next_bomb.append([i,j])
            else:
                graph[i][j] = "O"

def explode_bomb():
    while next_bomb:
        tx, ty = next_bomb.pop()
        graph[tx][ty] = "."
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < R and 0<= ny < C:
                graph[nx][ny] = "."


for i in range(R):
    temp = str(input())
    for j in range(C):
        graph[i][j] = temp[j]
time = 1
while time < N:
    set_bomb()
    time += 1
    if time >= N:
        break
    explode_bomb()
    time += 1

for i in range(R):
    for j in range(C):
        print(graph[i][j], end = "")
    print()
