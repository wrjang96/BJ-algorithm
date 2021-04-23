import sys
N = int(sys.stdin.readline())
dp = [[0,0] for i in range(46)]
dp[0] = (1,0)
dp[1] = (0,1)
if N == 1:
    print(0,1)
else:
    for i in range(2,N+1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    print(dp[N][0],dp[N][1])
#
# import sys
# N = int(sys.stdin.readline())
# dp = [(0,0) for i in range(46)]
# dp[0] = (1,0)
# dp[1] = (0,1)
#
# def recursive(x):
#     if dp[x] == (1,0):
#         return 1,0
#     if dp[x] == (0,1):
#         return 0,1
#     if dp[x] != (0,0):
#         return dp[x][0],dp[x][1]
#     px, py = recursive(x-1)
#     nx = py
#     ny = px+py
#     dp[x] = (nx,ny)
#     return nx,ny
# tmpx, tmpy = recursive(N-1)
# print(tmpx,tmpy)