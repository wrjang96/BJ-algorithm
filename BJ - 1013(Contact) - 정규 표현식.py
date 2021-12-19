import re

N = int(input())
ans = re.compile('(100+1+|01)+')
for i in range(N):
    tmp = input()
    if ans.fullmatch(tmp):
        print("YES")
    else:
        print("NO")
