import sys
N, M = map(int, input().split())

#원래 매트릭스 받기
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (N + 1) for i in range(N+1)]
#열별로 sum한 매트릭스 따로 만들어주기 
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + graph[i][j]

#행별 합 출력
for i in range(M):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    print(dp[ex][ey] - dp[sx -1][ey] - dp[ex][sy-1] + dp[sx-1][sy-1])




