t = int(input())

MIN = float('-inf')

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [MIN] * (n+1)
    dp[1] = arr[0]

    if n > 1:
        for i in range(2, n+1):
            dp[i] = max(arr[i-1], arr[i-1]+dp[i-1])

    print(max(dp))