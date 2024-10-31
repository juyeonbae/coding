import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0] * (n+1)
for p in range(1, n+1):
    pre[p] = pre[p-1] + arr[p-1]

for t in range(m):
    i, j = map(int, input().split())
    print(pre[j] - pre[i-1])