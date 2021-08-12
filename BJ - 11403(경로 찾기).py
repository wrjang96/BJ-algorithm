import sys
input = sys.stdin.readline
N = int(input())
undirected_graph = [[int(1e9)] * N  for _ in range(N)]
for i in range(N):
    undirected_graph[i] = list(map(int,input().split()))
for i in range(N):
    for j in range(N):
        if undirected_graph[i][j] == 0:
            undirected_graph[i][j] = int(1e9)
for k in range(N):
    for i in range(N):
        for j in range(N):
            undirected_graph[i][j] = min(undirected_graph[i][j], undirected_graph[i][k] + undirected_graph[k][j])

for i in range(N):
    for j in range(N):
        if undirected_graph[i][j] == int(1e9):
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()