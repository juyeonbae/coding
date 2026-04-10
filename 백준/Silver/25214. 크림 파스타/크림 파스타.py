import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
mn = arr[0] 

for i in range(1, n):
    if arr[i] < mn:
        mn = arr[i] 
        
    dp[i] = max(dp[i-1], arr[i]-mn)

print(*dp)
