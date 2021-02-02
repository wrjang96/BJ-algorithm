from sys import stdin
N,K = map(int,stdin.readline().split())
totup =1
totdown =1
if K > N-K:
    #print('1')
    for i in range(K+1, N+1,1):
        totup *= i
    for j in range(N-K,0,-1):
        totdown *= j
    #print(totup)
    #print(totdown)
    print(totup//totdown)
else:
    #print('2')
    for i in range(N-K+1, N+1,1):
        totup *= i
    for j in range(K,0,-1):
        totdown *= j
    #print(totup)
    #print(totdown)
    print(totup // totdown)
