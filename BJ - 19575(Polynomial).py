import sys
input = sys.stdin.readline
bottom = 10**9 + 7
N, X = map(int, input().split())
arr = [0] * (N + 1)

for i in range(N + 1):
    tmp1, tmp2 = map(int, input().split())
    arr[N - tmp2] = tmp1

result = arr[0] * X + arr[1]
for i in range(1, len(arr)-1):
    result = (result * X + arr[i+1]) % bottom
print(result % bottom)
