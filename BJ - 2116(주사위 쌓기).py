from sys import stdin
N = int(stdin.readline())
graph = [[0] * (6) for i in range(N)] # 주사위의 값 담아두는 배열
answer = [] # 옆면 담아두는 배열

for i in range(N):
    graph[i] = list(map(int,stdin.readline().split()))

uplist = [] # 위를 바라보는 면 담는 리스트
for k in range(0, 6, 1):
    uplist.append(graph[0][k]) # 이 면이 위를 봄
    # 0과5 1과3 2와4가 한쌍
    if k == 0:
        answer.append([graph[0][1], graph[0][2], graph[0][3], graph[0][4]])
    if k == 5:
        answer.append([graph[0][1], graph[0][2], graph[0][3], graph[0][4]])
    if k == 1:
        answer.append([graph[0][0], graph[0][2], graph[0][5], graph[0][4]])
    if k == 3:
        answer.append([graph[0][0], graph[0][2], graph[0][5], graph[0][4]])
    if k == 4:
        answer.append([graph[0][0], graph[0][1], graph[0][3], graph[0][5]])
    if k == 2:
        answer.append([graph[0][0], graph[0][1], graph[0][3], graph[0][5]])
   # print(uplist)
    for i in range(1, N, 1):
        up = uplist.pop(0) # 매번 위를 보는 주사위 면 갱신
        for j in range(6):
            if graph[i][j] == up:
                if j == 0:
                    answer.append([graph[i][1], graph[i][2], graph[i][3], graph[i][4]]) # 생각해보니 여기다 걍 Max할껄 싶기도
                    uplist.append(graph[i][5]) # 반대되는 면 위의 값에 추가
                if j == 5:
                    answer.append([graph[i][1], graph[i][2], graph[i][3], graph[i][4]])
                    uplist.append(graph[i][0])
                if j == 1:
                    answer.append([graph[i][0], graph[i][2], graph[i][5], graph[i][4]])
                    uplist.append(graph[i][3])
                if j == 3:
                    answer.append([graph[i][0], graph[i][2], graph[i][5], graph[i][4]])
                    uplist.append(graph[i][1])
                if j == 4:
                    answer.append([graph[i][0], graph[i][1], graph[i][3], graph[i][5]])
                    uplist.append(graph[i][2])
                if j == 2:
                    answer.append([graph[i][0], graph[i][1], graph[i][3], graph[i][5]])
                    uplist.append(graph[i][4])
    uplist.clear() # 이거 때문에 틀림

answersum =0
sum =0

for i in range(1, len(answer)+1, 1):
    sum +=max(answer[i-1]) # 4개의 면 중 최댓값 구해서
    if(i %N ==0): # 쌓인 주사위 마다 업데이트해서
        answersum = max(answersum,sum) # 대소 비교
        sum =0

print(answersum)