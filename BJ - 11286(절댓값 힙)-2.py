import sys
import heapq
N = int(sys.stdin.readline())
arr =[]

while(N):
    a = int(sys.stdin.readline())
    if a ==0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr,[abs(a),a])
    N-=1
