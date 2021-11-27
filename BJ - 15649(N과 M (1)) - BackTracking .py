import sys
input = sys.stdin.readline

def backtrack(x):
    if x == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if visited[i] == 0 and i not in arr:
            arr.append(i)
            backtrack(x + 1)
            arr.pop()
            for j in range(i, N):
                visited[j] = 0

N, M = map(int, input().split())
visited = [0] * (N + 1)
arr = []
backtrack(0)
