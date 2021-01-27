from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
MAP = [[0] * (N) for i in range(N)] # 나를 0으로 N-1 * N-1 개씩 놓은  배열
visited = [[0] for i in range(N)] # 방문 여부 확인
queue =[]
ans =[] # 정답의 개수 출력 위한 배열

def bfs(x):
    queue.append(0)
    wedding = 0
    cnt = 0
    while queue:
        k = queue[0]
        visited[0] = 1 # 첫 방문 배열 방문 쳌
        if(cnt > wedding): # 저장한 본인 친구의 수만큼만 반복문 돌아감
            break
        for i in range(0,N,1):
            if visited[i] == [0] and MAP[k][i] == 1:
                visited[i] = 1
                queue.append(i)
                ans.append(i)
        if cnt == 0:
            wedding += len(ans) # 본인의 친구의 수 저장
        queue.pop(0)
        cnt += 1
#입력
while M:
    fromv, tov =map(int , stdin.readline().split())
    MAP[fromv-1][tov-1] = 1
    MAP[tov-1][fromv-1] = 1
    M -= 1

bfs(0)
print(len(ans))