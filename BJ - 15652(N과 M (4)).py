from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = [_ for _ in range(1, N + 1)]
answer =[]

temp = list(combinations_with_replacement(arr, M))
for i in range(len(temp)):
    print(*temp[i])