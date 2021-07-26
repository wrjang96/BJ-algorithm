import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
V,E = map(int,input().split())
graph = [[]for i in range(V)]
reverse_graph = [[]for i in range(V)]
for i in range(E):
    start, end = map(int,input().split())
    start -=1
    end -= 1
    graph[start].append(end)
    reverse_graph[end].append(start)

stack = []
def dfs(node, visited, stack):
    visited[node] = 1
    for temp in graph[node]:
        if visited[temp] ==0:
            dfs(temp, visited,stack)
    stack.append(node)


def reverse_dfs(node, visited, result):
    visited[node] = 1
    result.append(node + 1)
    for temp in reverse_graph[node]:
        if visited[temp] == 0:
            reverse_dfs(temp, visited, result)

visited = [0] * (V)
for i in range(V):
    if visited[i] == 0:
        dfs(i, visited, stack)

answer = []
visited = [0] * (V)
while stack:
    temp = stack.pop(-1)
    result = []
    if visited[temp] == 0:
        reverse_dfs(temp, visited, result)
        answer.append(sorted(result))
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(*answer[i],end=" ")
    print(-1)
