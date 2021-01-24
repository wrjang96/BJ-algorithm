#BJ - 1620(나는야 포켓몬 마스터 이다솜)
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr =[]
while(N):
    temp = input()
    arr.append(temp.strip())
    N-=1

while(M):
    temp2 = input().strip()
    if(temp2.isdigit()):
        print(arr[int(temp2)-1])
    else :
        print(arr.index(temp2)+1)
    M-=1
