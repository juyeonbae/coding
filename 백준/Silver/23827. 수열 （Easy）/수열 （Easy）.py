import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

MOD = 1000000007

s, ans = 0, 0
for i in a:
    ans += s * i
    s += i 

print(ans % MOD)