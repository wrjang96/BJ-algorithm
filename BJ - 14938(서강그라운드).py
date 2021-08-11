import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0,start))
    distance[start][start] = 0
    while (len(queue) > 0):
        dist, now = heapq.heappop(queue)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

if __name__ == "__main__":
    N, M, R = map(int, input().split())
    item_num = list(map(int, input().split()))
    graph = [[] for i in range(N)]
    distance = [[int(1E9)] * N for i in range(N)]
    for _ in range(R):
        A, B, L = map(int, input().split())
        A -= 1
        B -= 1
        graph[A].append((B, L))
        graph[B].append((A, L))
    answer = [0] * N
    for i in range(N):
        dijkstra(i)
    for i in range(N):
        for j in range(N):
            if distance[i][j]<=M:
                answer[i] += item_num[j]
    print(max(answer))
    #print(distance)

