# x좌표와 y좌표가 특이하게 되어있어, 변환하는게 핵심

import sys
input = sys.stdin.readline
A,B = map(int,input().split())
N,M = map(int,input().split())
graph = [[0] * A for i in range(B)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
robot = []
robot2 =[]


# 여기가 핵심
while (N):
    startx, starty, way = map(str, input().split())
    robot.append([B-int(starty),int(startx)-1, way])
    robot2.append([B-int(starty),int(startx)-1])
    graph[B-int(starty)][int(startx)-1] = 1
    N-=1


endflag =0
while (M):
    robot_name, order, num = map(str,input().split())
    sx = robot[int(robot_name) - 1][0]
    sy = robot[int(robot_name) - 1][1]
    flag = robot[int(robot_name) - 1][2]
    queue =[]
    num = int(num)
    if order == 'R':
        while(num):
            if robot[int(robot_name) - 1][2] == 'N':
                robot[int(robot_name) - 1] = [sx, sy, 'E']
            elif robot[int(robot_name) - 1][2] == 'E':
                robot[int(robot_name) - 1] = [sx, sy, 'S']
            elif robot[int(robot_name) - 1][2] == 'W':
                robot[int(robot_name) - 1] = [sx, sy, 'N']
            elif robot[int(robot_name) - 1][2] == 'S':
                robot[int(robot_name) - 1] = [sx, sy, 'W']
            num -= 1
    elif order == 'L':
        while (num):
            if robot[int(robot_name) - 1][2] == 'N':
                robot[int(robot_name) - 1] = [sx, sy, 'W']
            elif robot[int(robot_name) - 1][2] == 'E':
                robot[int(robot_name) - 1] = [sx, sy, 'N']
            elif robot[int(robot_name) - 1][2] == 'W':
                robot[int(robot_name) - 1] = [sx, sy, 'S']
            elif robot[int(robot_name) - 1][2] == 'S':
                robot[int(robot_name) - 1] = [sx, sy, 'E']
            num-=1

    elif order == 'F':
        queue.append([sx, sy, flag])
        graph[sx][sy] = 0
        while (num):
            x,y, z = queue.pop(0)
            if order == 'F':
                if z == 'N':
                    nx = x -1
                    ny = y
                elif z == 'E':
                    nx = x
                    ny = y + 1
                elif z == 'W':
                    nx = x
                    ny = y - 1
                elif z == 'S':
                    nx = x + 1
                    ny = y
                if (0 <= nx < B and 0 <= ny < A and [nx, ny] not in robot2):
                    queue.append([nx, ny, z])
                    robot[int(robot_name) - 1] = [nx, ny, z]
                    graph[nx][ny] =1
                    robot2[int(robot_name) - 1] = [nx, ny]
                else:
                    if [nx, ny] in robot2:
                        print("Robot", int(robot_name), "crashes into robot", robot2.index([nx, ny]) + 1)
                        endflag = 1
                        break
                    elif 0 > nx or nx >= B or 0 > ny or ny >= A:
                        print("Robot", int(robot_name), "crashes into the wall")
                        endflag = 1
                        break
            num -= 1
    if endflag == 1:
        break
    M-=1

if endflag == 0:
    print('OK')
