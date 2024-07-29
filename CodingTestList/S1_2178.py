# S1_2178_미로 탐색.py

from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        # 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 범위 내에 있고 이동할 수 있는 경우
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N - 1][M - 1]


# main
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# 방향 벡터 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
