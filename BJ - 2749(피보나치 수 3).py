N = int(input())

mod = 10 ** 6
dp = [0, 1]
p = (mod//10)*15

for i in range(2,p):
    dp.append(dp[i-1]+dp[i-2])
    dp[i] %= mod

print(dp[N%p])