import sys
input = sys.stdin.readline
N,M = map(int,input().split())
testcase = int(input())
tmp1 = []
tmp2 = []
tmp1.append(0)
tmp1.append(M)
tmp2.append(0)
tmp2.append(N)
for i in range(testcase):
    s,e = map(int, input().split())
    if s == 0:
        tmp1.append(e)
    else:
        tmp2.append(e)

tmp1.sort()
tmp2.sort()
maxtmp1 = 0
maxtmp2 = 0
for i in range(1, len(tmp1)):
    maxtmp1 = max(maxtmp1, (tmp1[i] - tmp1[i-1]))
for i in range(1, len(tmp2)):
    maxtmp2 = max(maxtmp2, (tmp2[i] - tmp2[i - 1]))
print(maxtmp1 *  maxtmp2)


