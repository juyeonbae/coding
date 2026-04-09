n = int(input())
MOD = 1000000007

dp = [0] * (n+1)
if n == 0: print(0)
if n == 1 or n == 2: print(1)
if n > 3:
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD

    print(dp[n])