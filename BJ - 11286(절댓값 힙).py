import sys
import heapq
N = int(sys.stdin.readline())
plus =[]
minus =[]

while(N):
    a = int(sys.stdin.readline())
    if(a>0):
        heapq.heappush(plus,a)
    elif(a==0):
        if len(plus)==0 and len(minus)==0:
            print(0)
        elif len(plus)==0 and len(minus) !=0:
            print(heapq.heappop(minus)*-1)
        elif len(minus)==0 and len(plus) !=0:
            print(heapq.heappop(plus))
        else:
            if(abs(plus[0])==abs(minus[0])):
                print(heapq.heappop(minus)*-1)
            else:
                if(abs(plus[0])>abs(minus[0])):
                    print(heapq.heappop(minus)*-1)
                else:
                    print(heapq.heappop(plus))
    else:
        heapq.heappush(minus,a*-1)
    N-=1
    #print(plus)
    #print(minus)
