import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
arr = [['.'] * n for _ in range(n)]

sx, sy = r-1, c-1

for i in range(n):
    for j in range(n):
        if (i+j)%2 == (sx+sy)%2:
            arr[i][j] = 'v'

for row in arr:
    print(''.join(row))
