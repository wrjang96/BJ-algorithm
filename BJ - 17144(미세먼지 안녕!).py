import sys
from copy import deepcopy
input = sys.stdin.readline
R,C,T = map(int,input().split())
graph = [[0] * C for i in range(R)]
dx =[-1,0,1,0]
dy = [0,-1,0,1]
aircon = [] # 공기청정기 위치 저장
for i in range(R):
    graph[i] = list(map(int,input().split()))

def clear(): # 미세먼지 확산
    temp = deepcopy(graph)
    for i in range(R):
        for j in range(C):
            if temp[i][j] ==-1:
                aircon.append((i,j))
            if temp[i][j] > 0:
                cnt =0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    dust = temp[i][j] //5
                    if 0<=nx<R and 0<=ny<C and temp[nx][ny] != -1 :
                        graph[nx][ny] += dust
                        cnt +=1
                graph[i][j] -=(dust *cnt)

def circulate(graph): # 청정기 돌아감
    temp2 = deepcopy(graph)
    # 위쪽 공기 순환
    upperx, uppery = aircon[0]
    temp2[upperx].insert(0,-1)
    temp2[upperx][uppery+1] =0
    corner1 = temp2[upperx].pop(-1)
    for i in range(upperx-1,-1,-1):
        temp2[i][-1], corner1 = corner1,temp2[i][-1]
    temp2[0].insert(C-1,corner1)
    corner1 = temp2[0].pop(0)
    for i in range(1,upperx,1):
        if temp2[i][0] == -1:
            break
        else:
            temp2[i][0], corner1 = corner1,temp2[i][0]
    #아래쪽 공기 순환
    downx, downy = aircon[1]
    temp2[downx].insert(0, -1)
    temp2[downx][downy + 1] = 0
    corner2 = temp2[downx].pop(-1)
    for i in range(downx+1, R, 1):
        temp2[i][-1], corner2 = corner2, temp2[i][-1]
    temp2[-1].insert(C - 1, corner2)
    corner2 = temp2[-1].pop(0)
    for i in range(R-2,downx-1,-1):
        if temp2[i][0] == -1:
            break
        else:
            temp2[i][0], corner2 = corner2,temp2[i][0]
    return temp2 # temp2 로 반환해서 graph 변환

for i in range(T):
    clear()
    graph = circulate(graph)

tot =0
for i in range(R):
    tot += sum(graph[i])
print(tot+2) # 청소기 -1의 값 * 2
