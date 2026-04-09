t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    
    if n == 0 or n == 1: print(1)
    if n == 2: print(2)
    if n == 3: print(4) 
    if n > 3:
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
        
        print(dp[n])

