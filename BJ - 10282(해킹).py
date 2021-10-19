import heapq
import sys; input = sys.stdin.readline
testcase = int(input())
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
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


while testcase:
    n, d, c = map(int, input().split())
    c -= 1
    graph = [[]for i in range(n)]
    distance = [int(1E9)] * n
    for i in range(d):
        a,b,weight = map(int, input().split())
        a -= 1; b -= 1
        graph[b].append((a,weight))
    dijkstra(c)
    cnt = 0
    max_flag = 0
    for temp in distance:
        if temp != int(1E9):
            cnt +=1
            max_flag = max(max_flag, temp)

    print(cnt,max_flag)
    testcase -= 1