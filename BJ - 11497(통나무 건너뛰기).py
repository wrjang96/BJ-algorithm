import sys
import heapq
input = sys.stdin.readline
arr = []
testcase = int(input())
for tc in range(testcase):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    answer = []
    tx = arr.pop()
    answer.append(tx)
    flag = True
    while arr:
        tmp = arr.pop()
        if flag == True:
            answer.append(tmp)
            flag = False
        else:
            answer.insert(0, tmp)
            flag = True
    for i in range(len(answer)):
        ans = max(abs(answer[i] - answer[i - 1]), ans)
    print(ans)