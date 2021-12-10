import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0] * (N+ 1)
for i in range(1, N+1):
    sum[i] = arr[i-1] + sum[i-1]

for i in range(M):
    s, e = map(int, input().split())
    s -= 1
    print(sum[e] - sum[s])

