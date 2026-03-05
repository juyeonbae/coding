import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

P = [0] * n

for i in range(1, n):
    P[i] = abs(a[i] - a[i-1]) + P[i-1]

out = []
for i in range(q):
    s, e = map(int, input().split())
    out.append(P[e-1] - P[s-1])

print('\n'.join(map(str, out)))
    