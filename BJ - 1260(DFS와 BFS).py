def dfs(x):
    print(x, end=' ')
    visited[x]+=1
    for i in range(1,N+1,1):
        if(visited[i]==0 and MAP[i][x]):
            dfs(i)

def bfs():
    queue.append(V)
    visited[V] +=1
    while queue:
        print(queue[0], end=' ')
        for i in range(1,N+1,1):
            if visited [i] ==0 and MAP[i][queue[0]]==1:
                queue.append(i)
                visited[i]+=1
        del queue[0]

queue =[]             
N, M, V = map(int, input().split())
MAP = [[0] * (N + 1) for i in range(N + 1)]
visited = [0 for i in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    MAP[x][y] = 1
    MAP[y][x] = 1
    
dfs(V)
print()
visited = [0 for i in range(N + 1)]
bfs()
