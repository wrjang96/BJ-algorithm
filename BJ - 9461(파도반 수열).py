import sys
input = sys.stdin.readline
testcase = int(input())
dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(3, 101,1):
    dp[i] = dp[i-2] + dp[i-3]

while testcase :
    N = int(input())
    print(dp[N-1])
    testcase -=1


