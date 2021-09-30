from collections import deque
N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
graph = [int(1e9)] * 100001
queue = deque([N])
graph[N] = 0

while queue:
    temp = queue.popleft()
    if 0 <= temp * 2 <= 100000:
        if visited[temp * 2] == 0:
            queue.appendleft(temp * 2)
            visited[temp * 2] = 1
            graph[temp*2] = graph[temp]
    if 0 <= temp + 1 <= 100000:
        if visited[temp + 1] == 0:
            queue.append(temp + 1)
            visited[temp + 1] = 1
            graph[temp + 1] = graph[temp] + 1
    if 0 <= temp - 1 <= 100000:
        if visited[temp - 1] == 0:
            queue.append(temp - 1)
            visited[temp - 1] = 1
            graph[temp - 1] = graph[temp] + 1
print(graph[K])