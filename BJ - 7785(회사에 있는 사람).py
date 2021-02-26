import sys
input = sys.stdin.readline
N = int(input())
worklist =[]
while N:
    data1,data2 = map(str,input().split())
    if data2 == 'leave':
        worklist.remove(data1)
    if data2 == 'enter':
        worklist.append(data1)
    N-=1
worklist.sort(reverse = True)

for i in range(len(worklist)):
    print(worklist[i])