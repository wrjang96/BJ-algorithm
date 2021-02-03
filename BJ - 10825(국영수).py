from sys import stdin
N = int(stdin.readline())
answer =[]
while N:
    name, kor, eng, math = map(str, stdin.readline().split())
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    answer.append([-kor,eng,-math,name])
    N-=1
answer.sort()

for i in range(len(answer)):
    print(answer[i][3])