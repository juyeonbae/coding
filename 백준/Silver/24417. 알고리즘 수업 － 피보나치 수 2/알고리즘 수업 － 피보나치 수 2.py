import sys
input = sys.stdin.readline

n = int(input())
MOD = 1000000007

a = b = 1
for i in range(3, n+1):
    a, b = b, (a+b) % MOD

ans1 = b 
ans2 = (n-2) % MOD

print(ans1, ans2)