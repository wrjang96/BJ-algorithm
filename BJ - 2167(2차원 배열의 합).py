import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * M for i in range(N)]
sum_arr = [[0] * (M+1) for i in range(N+1)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(M):
        sum_arr[i+1][j+1] += arr[i][j] + sum_arr[i+1][j]+ sum_arr[i][j+1] - sum_arr[i][j]

# print(sum_arr)
K = int(input())
for i in range(K):
    sx,sy,ex,ey = map(int, input().split())
    # print(sum_arr[ex][ey],sum_arr[sx - 1][ey], sum_arr[ex][sy - 1] ,sum_arr[sx - 1][sy - 1])
    print(sum_arr[ex][ey] - sum_arr[sx-1][ey] - sum_arr[ex][sy-1] + sum_arr[sx-1][sy-1])

# 4 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 1
# 2 2 3 4