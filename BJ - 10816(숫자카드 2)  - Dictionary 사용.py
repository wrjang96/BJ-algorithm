import sys
input = sys.stdin.readline
database = {}
N = int(input())
arr1 = list(map(int,input().split()))
for i in range(N):
    if arr1[i] not in database:
        database[arr1[i]] = 1
    else:
        database[arr1[i]] += 1
M = int(input())
arr2 = list(map(int,input().split()))
for i in range(M):
    if arr2[i] not in database:
        print(0, end=" ")
    else:
        print(database[arr2[i]], end=" ")