import sys; sys.stdin.readline
N = int(input())
M = int(input())
root = [i for i in range(N+1)]
def union(x,y):
    tx = find(x)
    ty = find(y)
    if tx != ty:
        root[tx] = ty

def find(x):
    if x == root[x]:
        return root[x]
    else:
        y = find(root[x])
        root[x] = y
        return y

for i in range(M):
    x, y = map(int, input().split())
    for j in range(x, y):
        union(j,j+1)

answer = set()
for i in range(1,N+1):
    tx = find(i)
    answer.add(tx)

print(len(answer))