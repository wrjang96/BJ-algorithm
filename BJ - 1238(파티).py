import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N,M,X = map(int, input().split())
graph = [[] for i in range(N+1)]

answer = [0]* (N+1)
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0,start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost, i[0]))
    if start == X:
        for i in range(1, N + 1):
            answer[i] += distance[i]
    else:
        answer[start] +=distance[X]



for i in range(1, N+1):
    distance = [INF] * (N + 1)
    dijkstra(i)

print(max(answer))