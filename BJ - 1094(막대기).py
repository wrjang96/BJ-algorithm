N = int(input())
arr = [0] * 7
for i in range(6, -1, -1):
    if 2 ** i <= N and N < 2 ** (i + 1) :
        N -= 2 ** i
        arr[i] += 1
print(sum(arr))