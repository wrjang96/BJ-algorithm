import sys
input = sys.stdin.readline

N = int(input())
graph = [[int(1e9)] * N  for _ in range(N)]
while 1:
    input_start, input_end = map(int,input().split())
    if input_start == -1 and  input_end == -1:
        break
    input_start -= 1
    input_end -= 1
    graph[input_start][input_end] = 1
    graph[input_end][input_start] = 1
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
            
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j]= min(graph[i][j], graph[i][k] + graph[k][j])

temp_cnt = 0
temp_f = int(1e9)
answer = []
for i in range(N):
    if temp_f > max(graph[i]):
        answer.clear()
        temp_cnt = 0
    temp_f = min(temp_f, max(graph[i]))
    if temp_f == max(graph[i]):
        temp_cnt +=1
        answer.append(i + 1)

#print(graph)
print(temp_f, temp_cnt)
print(*answer)
