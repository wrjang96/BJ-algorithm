import sys
input = sys.stdin.readline

N = int(input())
arr = []
answer = []
cnt = 0
for i in range(N):
    temp = int(input())
    if temp == i + 1:
        cnt += 1
        answer.append(temp)
    else:
        arr.append([i+1, temp])
for i in range(len(arr)):
    for j in range(i):
        if arr[i][0] == arr[j][1] and arr[j][0] == arr[i][1]:
            cnt += 2
            answer.append(arr[i][0])
            answer.append(arr[j][0])

print(cnt)
answer.sort()
for i in range(len(answer)):
    print(answer[i])