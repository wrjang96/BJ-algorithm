import sys
input = sys.stdin.readline
lumber = []

N, M = map(int, input().split())
lumber = list(map(int, input().split()))
answer = []
left = 0
right = max(lumber)
lumber.sort(reverse = True)

while left<=right:
    mid = (left+right)//2
    temp_sum =0
    for i in range(N):
        tmp = lumber[i] - mid
        if tmp <=0:
            break
        else:
            temp_sum += tmp
    if temp_sum == M:
        answer.append(mid)
        break
    elif temp_sum > M:
        left = mid + 1
        answer.append(mid)
    else:
        right = mid - 1

print(max(answer))


