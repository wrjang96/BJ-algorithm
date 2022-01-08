import sys
from itertools import permutations
input = sys.stdin.readline
N,M = map(int, input().split())
arr = list(map(int, input().split()))
# arr = set(arr); arr = list(arr)
arr.sort()
temp = list(set(permutations(arr,M)))
temp.sort()
for tmp in temp:
    print(*tmp)