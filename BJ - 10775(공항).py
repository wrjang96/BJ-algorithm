import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
G= int(input())
P= int(input())
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

parent = { }

for i in range(0,G+1):
    parent[i] = i
result =0
while(P):
    tmp = find_parent(int(input()))
    if tmp ==0:
        break
    union_parent(tmp,tmp-1)
    result+=1
    P-=1
print(result)