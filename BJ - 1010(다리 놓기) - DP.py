import sys
input = sys.stdin.readline
T = int(input())
fact =[1]*31
for i in range(0, 31):
    for j in range(1,i+1):
        fact[i] *=j

while(T):
    N,M = map(int, input().split())
    tmp = fact[M] // (fact[N] * fact[M-N])
    print(tmp)
    T-=1