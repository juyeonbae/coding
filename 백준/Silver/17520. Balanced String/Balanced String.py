n = int(input())
dp = [0] * (n+1)
MOD = 16769023

dp[1] = 1
if n == 2: dp[2] = 1
if n > 2:
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-2] * 2 % MOD

print(dp[n] * 2 % MOD)