import heapq
heap=[]

N = int(input())
while N:
    data =int(input())
    heapq.heappush(heap,data)
    N-=1
result =0
while heap:
    temp1 = heapq.heappop(heap)
    if len(heap)==0:
        break
    temp2 = heapq.heappop(heap)
    result+=(temp1+temp2)
    if(len(heap)!=0):
        heapq.heappush(heap,temp1+temp2)

if N==1:
    print(0)
else:
    print(result)
