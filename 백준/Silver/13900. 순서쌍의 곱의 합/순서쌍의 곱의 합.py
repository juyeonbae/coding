import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s, ans = 0, 0
for x in arr:
    ans += s * x
    s += x

print(ans)