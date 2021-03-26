import sys
input = sys.stdin.readline
graph = []
max_weight =[]
N = int(input())
while N:
    graph.append(int(input()))
    N -= 1
graph.sort()

cnt = len(graph)
for temp in graph:
    max_weight.append(cnt * temp)
    cnt -= 1

print(max(max_weight))
