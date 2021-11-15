import sys, heapq
input=sys.stdin.readline

while 1:
    N, M = map(int, input().split())  # 정점, 간선 개수
    if N == 0 and M == 0:
        break
    visited = [0] * (N + 1)
    lst = [[] for _ in range(N + 1)]
    ans = 0
    sum = 0
    for i in range(M):
        temp = list(map(int, input().split()))
        lst[temp[0]].append((temp[2], temp[1]))
        lst[temp[1]].append((temp[2], temp[0]))
        sum += temp[2]
    que = [(0, 1)]
    while que:
        node = heapq.heappop(que)
        if not visited[node[1]]:
            visited[node[1]] = 1
            ans += node[0]
            for n in lst[node[1]]:
                heapq.heappush(que, n)

    print(sum - ans)

