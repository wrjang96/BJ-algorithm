import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
answer = []

for i in range(1, N):
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
flag = max(dp)
for i in range(N-1, -1, -1):
    if flag == dp[i]:
        answer.append(arr[i])
        flag -= 1

answer.reverse()
for i in range(len(answer)):
    print(answer[i], end=" ")
