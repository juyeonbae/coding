import sys
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
arr = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr[i][i] = 0
    
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

mn, person = INF, 0

for i in range(1, n+1):
    tmp = sum(arr[i][1:])
    
    if mn > tmp:
        mn = tmp
        person = i 

print(person)

