a, b = map(int,input().split())

mx = max(a, b)
mn = min(a, b)
n = mx - mn - 1

if mx - mn <= 1:
    n = 0

print(n)
for i in range(mn + 1, mx):
    print(i, end=' ')