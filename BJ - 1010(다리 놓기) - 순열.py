import sys
input = sys.stdin.readline
T = int(input())
while(T):
    answer = 1
    down = 1
    num1, num2 = map(int, input().split())
    for i in range(num2, num2 - num1, -1):
        answer *= i
    for j in range(num1,0,-1):
        down *= j
    print(answer//down)
    T -= 1