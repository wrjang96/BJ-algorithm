import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * N
arr =[]
for i in range(N):
    arr.append(int(input()))

if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0] + arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[1], arr[2] + arr[1], arr[0] + arr[2])
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])
    print(dp[N - 1])

# import sys
# input = sys.stdin.readline
# N = int(input())
# dp = [0] * 10001
# graph =[]
# while(N):
#     graph.append(int(input()))
#     N-=1
# print(graph)
# dp[0] = graph[0]
# dp[1] = graph[0] + graph[1]
# dp[2] = max(graph[0] + graph[2], graph[1] + graph[2])
#
# for i in range(3, N):
#     dp[i] = max(dp[i-2] + graph[i],dp[i-1] +  )