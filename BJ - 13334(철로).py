import sys
import heapq

input = sys.stdin.readline
N = int(input())
timeline = []
for i in range(N):
    i1, i2 = map(int,input().split())
    timeline.append([min(i1, i2),max(i1, i2)])
timeline.sort(key = lambda x : (x[1],x[0]))
D = int(input())
anscnt = 0
cnt_arr =[]
for tline in timeline:
    if tline[1] - tline[0] <= D:
        if not cnt_arr:
            heapq.heappush(cnt_arr, tline)
        else:
            while cnt_arr[0][0] < tline[1] - D:
                heapq.heappop(cnt_arr)
                if not cnt_arr:
                    break
            heapq.heappush(cnt_arr, tline)
    anscnt = max(len(cnt_arr), anscnt)
print(anscnt)