from sys import stdin
N,C = map(int,input().split())
M = int(stdin.readline())
graph = [C] * N
zero =  [0] * N
truck =[]

while M:
    fromv, tov,weight = map(int, input().split())
    truck.append([tov,-fromv,weight]) # 빨리도착하는 순서로, 늦게 나가는 순서로
    M-=1
truck.sort()
cnt =0
while truck:
    tov, fromv, weight =truck.pop(0)
    fromv *= -1
    if graph == zero:
        break
    if min(graph[fromv - 1:tov - 1]) - weight > 0:
        cnt +=weight
        for j in range(fromv - 1, tov - 1, 1):
            graph[j] -= weight
    else:
        if min(graph[fromv - 1:tov - 1])>= 0:
            tmp = min(graph[fromv - 1:tov - 1])
            for j in range(fromv - 1, tov - 1, 1):
                graph[j] -= tmp
            cnt += tmp
print(cnt)
#6 60
#5
#1 2 30
#2 5 70
#5 6 60
#3 4 40
#1 6 40
#150

