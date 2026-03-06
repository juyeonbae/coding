import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = list(map(int, input().split()))

window = sum(T[:m])
ans = window
for i in range(m, n):
    window += T[i] - T[i-m]
    if ans < window:
        ans = window

print(ans)