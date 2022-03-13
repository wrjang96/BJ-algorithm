from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
R,C,K = map(int, input().split())

graph = [[0] * C for i in range(R)]
queue = deque([])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
visited = [[0] * C for i in range(R)]
cnt = 0

def dfs(graph,visited,tx,ty,cnt):
    cnt += 1
    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]
        if nx == 0 and ny == C - 1:
            print(cnt)
            break
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and graph[nx][ny] == ".":
            dfs(graph,visited,nx,ny,cnt)
            visited[nx][ny] = 1



for i in range(R):
    temp = input()
    for j in range(C):
        graph[i][j] = temp[j]
print(graph[R-1][0], graph[0][C-1])
# queue.append([R - 1, 0])

visited[R - 1][0] = 1
dfs(graph, visited, R-1, 0,cnt)
print(graph)


