n, state = map(int, input().split())
a, b, c, d = map(float, input().split())

dp = [[0.0, 0.0] for _ in range(n+1)]

if state == 0: dp[1] = [a, b]
else: dp[1] = [c, d]

if n > 1:
    for i in range(2, n+1):
        dp[i][0] += dp[i-1][0] * a + dp[i-1][1] * c
        dp[i][1] += dp[i-1][0] * b + dp[i-1][1] * d

print(int(dp[n][0] * 1000+0.5))
print(int(dp[n][1] * 1000+0.5))