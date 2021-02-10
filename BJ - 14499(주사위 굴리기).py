# 시작점 좌표가 반대라 한번 틀림
def move(nx,ny,flag): # 주사위가 평면에서 이동하는 함수
    if flag == 1:
        nx +=dx[flag-1]
        ny +=dy[flag-1]
        return nx,ny
    elif flag == 2:
        nx +=dx[flag-1]
        ny +=dy[flag-1]
        return nx,ny
    elif flag == 3:
        nx +=dx[flag-1]
        ny +=dy[flag-1]
        return nx,ny
    elif flag == 4:
        nx +=dx[flag-1]
        ny +=dy[flag-1]
        return nx,ny

def calculation(x,y,flag,dice): # 주사위 면 돌아가는 함수
    if flag == 1:
        tmpdice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        dice = tmpdice
    elif flag == 2:
        tmpdice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        dice = tmpdice
    elif flag == 3:
        tmpdice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        dice = tmpdice
    elif flag == 4:
        tmpdice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        dice = tmpdice
    if graph[y][x] ==0: # 닿는 면이 0일 경우
        graph[y][x] = dice[5]
    else: # 그 외
        dice[5] = graph[y][x]
        graph[y][x] =0
    print(dice[0]) # 주사위의 맨 윗면
    return dice

N,M,Y,X,K = map(int,input().split())
graph = [[0] * M for i in range(N)]
for _ in range(N):
    graph[_] = list(map(int, input().split()))
order = list(map(int,input().split()))
dice = [0,0,0,0,0,0]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

while order: # 메인 함수
    flag = order.pop(0)
    nx, ny = move(X, Y, flag)
    if 0 <= nx < M and 0 <= ny < N:
        dice = calculation(nx, ny, flag, dice)
        X = nx
        Y = ny
    else:
        continue # 예외일 경우 XY 안바꾸고 그냥 SKIP