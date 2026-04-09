n = int(input())

arr = []
for _ in range(n):
    tmp = float(input())
    arr.append(tmp)

dp = [0] * (n+1)
dp[1] = arr[0]

if n > 1:
    for i in range(2, n+1):
        dp[i] = max(dp[i-1]*arr[i-1], arr[i-1])

print(f"{round(max(dp), 3):.3f}")