import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())
graph = [[]for i in range(N+1)]
distance = [[INF] * (N) for i in range(N+1)]
start_node = 1
end_node = N

while(E):
    fromv, tov, time = map(int, input().split())
    fromv -=1
    tov -=1
    graph[fromv].append((tov,time))
    graph[tov].append((fromv, time))
    E -=1

V1, V2 = map(int, input().split())
V1 -=1
V2 -=1
def dijkstra(start):
    queue =[]
    heapq.heappush(queue,(0,start))
    distance[start][start] =0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

for i in range(0,N,1):
    dijkstra(i)


if min((distance[0][V1]+distance[V1][V2]+distance[V2][N-1]),(distance[0][V2]+distance[V2][V1]+distance[V1][N-1])) >= INF:
    print(-1)
else:
    print(min((distance[0][V1]+distance[V1][V2]+distance[V2][N-1]),(distance[0][V2]+distance[V2][V1]+distance[V1][N-1])))
