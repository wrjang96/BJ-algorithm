import sys
from itertools import combinations # 조합을 써야함
# 처음 생각 dist 모두 계산 한 다음, M 의 수만큼 하나씩 뺄 계획
# but, 조합이 아닐 경우 예외 case 발생
# 그래서 조합을 썼어야 됨
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[0] * N for i in range(N)]

house =[]
chicken = []
distance =[]

for i in range(N):
    graph[i] = list(map(int,input().split())) # 입력 받으면서
    for j in range(len(graph[i])):
        if graph[i][j] == 2: # 치킨집 위치
            chicken.append([i,j])
        elif graph[i][j] == 1: # 집의 위치 저장
            house.append([i, j])

for combi in combinations(chicken, M):
    c_dist = 0
    sum = 0
    for j in range(len(house)):
        maxi = int(1e9)
        nx = house[j][0]
        ny = house[j][1]
        for i in combi:
            tmpx = i[0]
            tmpy = i[1]
            maxi = min(maxi,(abs(tmpx - nx) + abs(tmpy - ny)))
        sum += maxi
    c_dist += sum
    distance.append(c_dist)

distance.sort()
print(distance[0])