import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

dp[1] = 0
if n > 1:
    dp[2] = 1 
    for i in range(3, n+1):
        x = i//2
        dp[i] = x * (i-x) + dp[x] + dp[i-x]

print(dp[n])
