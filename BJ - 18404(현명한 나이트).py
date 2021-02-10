from sys import stdin
N,M = map(int,input().split())
X,Y = map(int,input().split())

result = []
#graph = [[0] * N for i in range(N)]
visited = set()
dx = [-2,-2,1,1,2,2,-1,-1]
dy = [-1,1,-2,2,-1,1,-2,2]
answer =[]
def bfs(x,y):
    queue =[]
    queue.append([x,y,0])
    result.append([x, y, 0])
    visited.add((x,y))
    while queue:
        px,py,tmpcnt = queue.pop(0)
        for i in range(8):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited:
                queue.append([nx, ny, tmpcnt+1])
                result.append([nx, ny, tmpcnt+1])
                visited.add((nx, ny))
            #print(queue)


bfs(X - 1, Y - 1)
while M:
    endx, endy = map(int, input().split())
    result.find
    for i in range(len(result)):
        if result[i][0] == endx -1  and result[i][1] == endy -1:
            answer.append(result[i][2])
            break
    M-=1

for i in range(len(answer)):
    print(answer.pop(0),end =' ')