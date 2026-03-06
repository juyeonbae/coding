import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())

T = [False] * n 
for i in range(b):
    x = int(input().strip())
    T[x-1] = True

window = sum(T[:k])
ans = window
for i in range(k, n):
    window += T[i] - T[i-k]
    if ans > window:
        ans = window

print(ans)
