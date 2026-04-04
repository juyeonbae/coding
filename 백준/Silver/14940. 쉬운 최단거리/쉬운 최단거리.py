import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x, y = i, j 
            dist[i][j] = 0

        elif arr[i][j] == 0:
            dist[i][j] = 0

q = deque([(x, y)])
visited[x][y] = True

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
            visited[nx][ny] = True

for i in range(len(dist)):
    print(*dist[i])
            