import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = []
dice = []
for i in range(N):
    temp = int(input())
    arr.append(temp)
cnt = 0
ans = 0
temp_num = 1
for i in range(M):
    temp = int(input())
    temp_num += temp
    print(temp_num, temp, arr[temp])
    if temp_num >= len(arr) -1:
        ans = cnt
        break
    cnt +=1
print(ans)

