import sys

input = sys.stdin.readline
N,M = map(int, input().split())
database = {}
for i in range(N):
    temp = input().rstrip()
    database[temp] = True

cnt = 0
for i in range(M):
    temp = input().rstrip()
    if temp in database:
        cnt += 1
print(cnt)
