import sys
input = sys.stdin.readline

N, X = map(int, input().split())
a = list(map(int, input().split()))

window = sum(a[:X])
ans = window

cnt = 1
for i in range(X, N):
    window += a[i] - a[i-X]
    if ans < window:
        ans = window
        cnt = 1
    elif ans == window:
        cnt += 1

if not ans:
    print('SAD')
else:
    print(ans)
    print(cnt)