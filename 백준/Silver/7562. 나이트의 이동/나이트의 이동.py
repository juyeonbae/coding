from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    r, c = map(int, input().split())
    tx, ty = map(int, input().split())

    q = deque()
    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]

    q.append((r, c))
    visited[r][c] = True

    while q:
        x, y = q.popleft()

        if x == tx and y == ty:
            break 

        dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
        dys = [-2, -1, 1, 2, 2, 1, -1, -2]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1

    if visited[tx][ty]:
        print(dist[tx][ty])