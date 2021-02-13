import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x: # 아마 여기서 재귀가 일어난듯
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
parent = { }

for i in range(0,N+1):
    parent[i] = i

while(M):
    flag, fromv, tov = map(int, input().split())
    if flag ==0:
        union_parent(fromv,tov)
    elif flag ==1:
        if find_parent(fromv) == find_parent(tov):
            print('YES')
        else:
            print('NO')
    M-=1
