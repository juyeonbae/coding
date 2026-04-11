import sys
input = sys.stdin.readline

dp = [0] * 501
dp[1] = 1
dp[2] = 2
for i in range(3, 501):
    dp[i] = dp[i-1] + dp[i-2]

while True:
    a, b  = map(int, input().split())
    if a == 0 and b == 0:
        sys.exit()

    cnt = 0
    for f in range(1, len(dp)):
        if dp[f] > b:
            break
        if dp[f] >= a:
            cnt += 1
            
    print(cnt)
        
    

