from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
conveyor_belt = list(map(int, input().split()))

for i in range(N * 2):
    temp = conveyor_belt[0]
    conveyor_belt.pop(0)
    conveyor_belt.append([temp, 0])
conveyor_belt = deque(conveyor_belt)

def rotation():
    if conveyor_belt[N-1][1] == 1:
        conveyor_belt[N - 1][1] = 0
    #1번
    shield, robot = conveyor_belt.pop()
    conveyor_belt.appendleft([shield, robot])
    if conveyor_belt[N-1][1] == 1:
        conveyor_belt[N - 1][1] = 0
    ## 2번
    for i in range(N-2, -1, -1):
        if conveyor_belt[i][1] == 1 and conveyor_belt[i+1][1] == 0 and conveyor_belt[i+1][0] >= 1:
            conveyor_belt[i][1] = 0
            conveyor_belt[i + 1][1] = 1
            conveyor_belt[i+1][0] -= 1
    if conveyor_belt[N-1][1] == 1:
        conveyor_belt[N - 1][1] = 0
    #3번
    if conveyor_belt[0][0] != 0:
        conveyor_belt[0][1] = 1
        conveyor_belt[0][0] -= 1



answer_cnt = 1
while (1):
    rotation()
    ## 4번
    temp_cnt = 0
    for i in range(N * 2):
        if conveyor_belt[i][0] == 0:
            temp_cnt += 1
    if temp_cnt >=K:
        break
    answer_cnt += 1

print(answer_cnt)
