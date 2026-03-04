import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

p = [0] * (n + 1)

for i in range(1, n+1):
    p[i] = arr[i-1] + p[i-1]

m = int(input())

tmp = []
for _ in range(m):
    i, j = map(int, input().split())

    x = p[j] - p[i-1]
    tmp.append(x)

print('\n'.join(map(str, tmp)))