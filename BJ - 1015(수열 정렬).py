import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
ans = []
P =[]
for i in range(len(A)):
    ans.append([A[i],i])
ans.sort()
for i in range(len(ans)):
    P.append([ans[i][1],i])
P.sort()
for i in range(len(P)):
    print(P[i][1], end =' ')