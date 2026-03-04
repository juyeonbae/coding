import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

p = [0] * (n+1)
for i in range(1, n+1):
    p[i] = arr[i-1] + p[i-1]

ans = []
for _ in range(q):
    L, R = map(int, input().split())
    x = p[R] - p[L-1]
    ans.append(x)

print('\n'.join(map(str, ans)))
    