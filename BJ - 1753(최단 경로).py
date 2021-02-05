import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int,input().split())
start = int(input())
graph = [[]for i in range(V+1)]
distance = [INF] * (V+1)

while(E):
    fromv, tov, time = map(int,input().split())
    graph[fromv].append((tov,time))
    E -=1

def dijkstra(start):
    queue =[]
    heapq.heappush(queue, (0, start))
    distance[start] =0
    while (len(queue)>0):
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
