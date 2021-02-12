import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result =[]
graph = [[0] * M for i in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

def find():
    for i in range(N): # 4*1
        for j in range(M-3):
            result.append(sum(graph[i][j:j+4]))
    for i in range(M): # 1 *4
        for j in range(N-3):
            result.append(graph[j][i]+ graph[j+1][i]+ graph[j+2][i]+ graph[j+3][i])
    for i in range(N-1): # 2 *2
        for j in range(M-1):
            result.append(graph[i][j]+graph[i+1][j]+graph[i][j+1]+graph[i+1][j+1])
    for i in range(N-1): # 2 *3
        for j in range(M-2):
            result.append(graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j])
            result.append(graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j+2])
            result.append(graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j+1])
            result.append(graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2] + graph[i][j + 2])
            result.append(graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2] + graph[i][j + 1])
            result.append(graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2] + graph[i][j])
            result.append(graph[i + 1][j] + graph[i + 1][j + 1] + graph[i][j + 1] + graph[i][j + 2])
            result.append(graph[i][j] + graph[i + 1][j + 1] + graph[i][j + 1] + graph[i+1][j + 2])
    for i in range(N-2): # 3 *2
        for j in range(M-1):
            result.append(graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 2][j + 1]) #위로 긴 ㄴ
            result.append(graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i][j + 1])
            result.append(graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 1][j + 1])
            result.append(graph[i][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 2][j + 1])
            result.append(graph[i][j+1] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 2][j])
            result.append(graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1] + graph[i][j]) # 아래로 긴 ㄱ
            result.append(graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1] + graph[i+2][j])  # 아래로 긴 ㄱ
            result.append(graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1] + graph[i + 1][j])

find()
result.sort()
print(result[-1])

