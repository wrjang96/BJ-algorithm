import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[]for i in range(N + 1)]
distance = [int(1E9)] * (N + 1)
went = [[] for i in range(N + 1)]

for i in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while len(queue) > 0:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                went[i[0]] = []
                for j in went[now]:
                    went[i[0]].append(j)
                went[i[0]].append(i[0])
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

ts, te = map(int, input().split())
went[ts].append(ts)
dijkstra(ts)

print(distance[te])
print(len(went[te]))
print(*went[te])
