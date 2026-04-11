import sys
input = sys.stdin.readline

MOD = 1000000000

n = int(input())

dp = [0] * (abs(n)+1)

m = abs(n)
if m == 1: dp[1] = 1
if m > 1:
    dp[1] = 1
    for i in range(2, m+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD

if n < 0 and m % 2 == 0: print(-1)
elif n == 0: print(0)
else: print(1)

print(dp[m])