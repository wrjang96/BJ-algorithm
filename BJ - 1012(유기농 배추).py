import sys 
sys.setrecursionlimit(10000)



testcase= int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and farm[nx][ny]==1:
            visited[nx][ny] = 1
            dfs(nx,ny)


for i in range(testcase):
    cnt =0
    M,N,K = map(int,input().split())
    farm =[[0]*M for i in range(N)]
    #print(farm)
    visited =[[0]*M for i in range(N)]
    for j in range(K):
        a,b = map(int,input().split())
        farm[b][a] =1
    for x in range(N): #행
        for y in range(M): #
            if farm[x][y]==1 and visited[x][y] ==0:
                visited[x][y] ==1
                dfs(x,y)
                cnt+=1
    print(cnt)
        
