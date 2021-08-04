H, W, X, Y = map(int,input().split())
arr = [[0] for i in range(H + X)]
answer = [[0] * W for i in range(H)]

for i in range(H + X):
    arr[i] = list(map(int,input().split()))

for i in range(H):
    for j in range(W):
        if i < X and j<W:
            answer[i][j] = arr[i][j]
        elif i < H and j<Y:
            answer[i][j] = arr[i][j]
        else:
            answer[i][j] = arr[i][j] - answer[i-X][j-Y]
for i in range(len(answer)):
    print(*answer[i])
