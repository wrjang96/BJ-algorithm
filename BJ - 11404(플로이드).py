import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N) for i in range(N)]

while(M):
    fromv, tov, time = map(int, input().split())
    fromv -=1
    tov-=1
    graph[fromv][tov] = min(graph[fromv][tov],time)
    M-=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if i ==j:
                graph[i][j] =0

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j],end =' ')
    print()