def solution(n):
    dp =[0] * 2001
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, 3):
            if i >= j:
                dp[i] += dp[i-j]

    return dp[n]%1234567