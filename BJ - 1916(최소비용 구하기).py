import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
graph = [[]for i in range(N+1)]
distance = [INF] * (N+1)

while(M):
    fromv, tov, time = map(int,input().split())
    fromv -=1
    tov -= 1
    graph[fromv].append((tov,time))
    M -=1
startv, endv= map(int,input().split())

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

dijkstra(startv-1)
print(distance[endv - 1])

