from itertools import permutations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]
ans = list(permutations(arr,M))
for an in ans:
    print(*an)