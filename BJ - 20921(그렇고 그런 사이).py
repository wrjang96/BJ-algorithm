import sys
input = sys.stdin.readline
N,K = map(int,input().split())
answer =[]

while(1):
    if (N <= K):
        answer.append(N)
        K -= (N-1)
        N-= 1
    else:
        answer.append(1 + K)
        for i in range(1, N + 1):
            if (i != 1 + K):
                answer.append(i)
        break

for i in range(len(answer)):
    print(answer[i],'', end ='')
