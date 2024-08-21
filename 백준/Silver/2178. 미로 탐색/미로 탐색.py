# S1_2178 미로 탐색.py
from collections import deque


# bfs
def bfs(x, y):
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                Q.append((nx, ny))

    return board[n - 1][m - 1]


# main
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

Q = deque()

# 하 우 상 좌 방향 / x가 행, y가 열
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs(0, 0))
