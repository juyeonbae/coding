import sys
input = sys.stdin.readline

MOD = 1000000007

n = int(input())

dp = [0] * (n+1)

if n == 0 or n == 1: print(1)
if n > 1:
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2] + 1) % MOD

    print(dp[n])