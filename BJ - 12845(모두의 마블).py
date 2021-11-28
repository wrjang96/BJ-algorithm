import sys
input = sys.stdin.readline
N = int(input())
arr =list(map(int, input().split()))
temp = max(arr)
ans = 0
cnt = 0
for i in arr:
    if temp == i and cnt == 0:
        cnt +=1
    else:
        ans += (temp + i)
print(ans)
