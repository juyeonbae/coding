# S1_1926 그림.py

from collections import deque

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

# 상하좌우 네 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

mx, num = 0, 0  # 그림의 최댓값, 그림의 수

for i in range(n):
    for j in range(m):
        # 0이거나 방문한 곳은 continue
        if board[i][j] != 1 or visit[i][j]:
            continue

        num += 1  # 그림의 개수 + 1
        Q = deque()
        visit[i][j] = 1  # (i, j)로 BFS 시작 준비
        Q.append((i, j))
        area = 0  # 그림의 넓이

        while Q:
            area += 1  # pop 하는 개수를 센다. (넓이)
            cur = Q.popleft()

            for dir in range(4):  # 인접한 곳 탐색
                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if visit[nx][ny] or board[nx][ny] != 1:
                    continue

                visit[nx][ny] = 1
                Q.append((nx, ny))

        mx = max(mx, area)  # area > mx 인 경우

print(num)
print(mx)
