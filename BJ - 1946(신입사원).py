import sys
import heapq
input=sys.stdin.readline
testcase = int(input())
heap = []
while testcase:
    cnt =1
    N = int(input())
    for i in range(N):
        first, second = map(int,input().split())
        heapq.heappush(heap, [first, second])
    firstidx,secondidx = heapq.heappop(heap)
    while(len(heap)>0):
        tempx,tempy = heapq.heappop(heap)
        if(secondidx>tempy):
            secondidx = tempy
            cnt+=1
    testcase-=1
    print(cnt)
