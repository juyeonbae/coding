import math

n = int(input())
dp = [0] * 16
dp[0] = 4
dp[1] = 9
for i in range(2, n+1):
    x = 2 * math.sqrt(dp[i-1]) - 1
    dp[i] = dp[i-1] + x * (x-1) - 4**(i-1)

print(int(dp[n]))
