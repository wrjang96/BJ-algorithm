N = int(input())
arr = [0] * N
arr[0] = 1
arr[1] = 2

for i in range(2, N):
    arr[i] = (arr[i-1] + arr[i-2]) % 10

print(arr[N-1] % 10)