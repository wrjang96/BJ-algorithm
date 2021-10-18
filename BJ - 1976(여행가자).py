import sys; input = sys.stdin.readline
N = int(input())
M = int(input())
parents = [i for i in range(N + 1)]

def Find(x):
    if x == parents[x]:
        return x
    else:
        y = Find(parents[x])
        parents[x] = y
        return y
def Union(x,y):
    x = Find(x)
    y = Find(y)
    if x !=y:
        parents[y] = x

for i in range(1,N+1):
    temp = list(map(int, input().split()))
    for j in range(0,len(temp)):
        if temp[j] == 1:
            Union(i,j+1)

answer = list(map(int, input().split()))
flag = True
for i in range(len(answer) - 1):
    if Find(answer[i]) != Find(answer[i+1]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")


