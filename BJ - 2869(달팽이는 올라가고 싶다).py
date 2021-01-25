from sys import stdin
A,B,V =map(int,stdin.readline().split())
if (V-A)%(A-B) ==0:
    print((V-A)//(A-B)+1)
else:
    print((V-A)//(A-B)+2)

