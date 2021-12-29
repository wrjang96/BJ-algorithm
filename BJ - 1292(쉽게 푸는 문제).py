import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = []
for i in range(46):
    for j in range(i):
        arr.append(i)

print(sum(arr[N-1:M]))