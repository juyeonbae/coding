# S1_2178 미로 탐색.py
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]  # 거리 배열 초기화

Q = deque()

# 하 우 상 좌 방향 / x가 행, y가 열
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q.append((0, 0))
dist[0][0] = 0

while Q:
    x, y = Q.popleft()

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if dist[nx][ny] >= 0 or board[nx][ny] != 1: continue

        dist[nx][ny] = dist[x][y] + 1
        Q.append((nx, ny))

print(dist[n-1][m-1] + 1)