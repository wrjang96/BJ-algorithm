from collections import deque
from sys import stdin
T = int(stdin.readline())
while T:
    p = input().replace('RR', '')
    n = int(input())
    number = input()[1:-1]
    if number:
        number = deque(list(map(int, number.split(','))))
    rflag = False
    for data in p:
        if data == 'R':
            rflag = not rflag
        elif data == 'D':
            if number:
                if rflag:
                    number.pop()
                else:
                    number.popleft()
            else:
                print('error')
                break
    else:
        number = list(number)
        if rflag:
            number = number[::-1]

        print("[", end="")
        print(",".join(list(map(str, number))), end="")
        print("]")
    T -= 1
