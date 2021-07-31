N,M = map(int,input().split())
arr = [[[0] * M]for i in range(N)]
answer = [[0] * M for i in range(N)]

for i in range(N):
    arr[i] = list(map(int,input().split()))

max_answer = 0

for i in range(N):
    for j in range(M):
        if i > 0 and j == 0:
            answer[i][j] = answer[i-1][j]
        elif i == 0 and j > 0:
            answer[i][j] = answer[i][j-1]
        else:
            answer[i][j] = max(answer[i-1][j], answer[i][j-1])
        if arr[i][j] == 1:
            answer[i][j] += 1
        max_answer = max(max_answer, answer[i][j])

print(max_answer)