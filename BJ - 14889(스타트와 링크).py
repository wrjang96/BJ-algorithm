import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
arr = [[0] * N for i in range(N)]
nums = [i for i in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

answer = 1E9
A_Teams = list(combinations(nums, N//2))
for A_Team in A_Teams:
    A_Team = list(A_Team)
    B_Team = list(set(nums).difference(A_Team))
    tempAs = combinations(A_Team, 2)
    tempBs = combinations(B_Team, 2)
    sumA = 0; sumB =0
    for tempA in tempAs:
        sumA += (arr[tempA[0]][tempA[1]] + arr[tempA[1]][tempA[0]])
    for tempB in tempBs:
        sumB += (arr[tempB[0]][tempB[1]] + arr[tempB[1]][tempB[0]])
    if answer > abs(sumA - sumB):
        answer = abs(sumA - sumB)
print(answer)