import sys
import copy
from itertools import combinations
input = sys.stdin.readline
N = int(input())
arr = [[0] * N for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
possible = []
teachers = []
student_num = 0
for i in range(N):
    arr[i] = list(map(str, input().split()))
    for j in range(N):
        if arr[i][j] == 'X':
            possible.append([i,j])
        elif arr[i][j] == 'T':
            teachers.append([i,j])
        elif arr[i][j] == 'S':
            student_num += 1

combis_possible = list(combinations(possible, 3))
answer_flag = False
for combi_possible in combis_possible:
    cnt = 0
    queue = copy.deepcopy(teachers)
    arr[combi_possible[0][0]][combi_possible[0][1]] = "O"
    arr[combi_possible[1][0]][combi_possible[1][1]] = "O"
    arr[combi_possible[2][0]][combi_possible[2][1]] = "O"
    while queue:
        tx,ty = queue.pop(0)
        for i in range(tx-1,-1,-1):
            if arr[i][ty] == "O":
                break
            if arr[i][ty] == "S":
                cnt += 1
        for i in range(tx, N):
            if arr[i][ty] == "O":
                break
            if arr[i][ty] == "S":
                cnt +=1
        for i in range(ty-1, -1,-1):
            if arr[tx][i] == "O":
                break
            if arr[tx][i] == "S":
                cnt +=1
        for i in range(ty, N):
            if arr[tx][i] == "O":
                break
            if arr[tx][i] == "S":
                cnt += 1
    if cnt == 0:
        answer_flag = True
    arr[combi_possible[0][0]][combi_possible[0][1]] = 'X'
    arr[combi_possible[1][0]][combi_possible[1][1]] = 'X'
    arr[combi_possible[2][0]][combi_possible[2][1]] = 'X'


if answer_flag == True:
    print("YES")
else:
    print("NO")