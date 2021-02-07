import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int,input().split())
graph = [[]for i in range(N+1)]
distance = [INF] * (N+1)
start_node = 1
end_node = N

while M:
    fromv, tov, time = map(int, input().split())
    graph[fromv].append((tov, time))# 양방향 append
    graph[tov].append((fromv, time))# 양방향 append
    M-=1
#print(graph)
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while (len(queue)>0):
        dist, now = heapq.heappop(queue)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            print(i)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start_node)

#for i in range(1, N+1,1):
print(distance[end_node])
#    sum +=distance[i]
