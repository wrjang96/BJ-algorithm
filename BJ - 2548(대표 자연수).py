N = int(input())
arr = sorted(list(map(int, input().split())))
q, r = divmod(N, 2)
print(arr[q+r-1])
