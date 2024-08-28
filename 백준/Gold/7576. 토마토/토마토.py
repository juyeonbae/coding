from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))
            dist[i][j] = 0

# 방향 벡터
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue:
    cur_x, cur_y = queue.popleft()
    for dir in range(4):
        nx, ny = cur_x + dx[dir], cur_y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and board[nx][ny] == 0:
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            queue.append((nx, ny))

ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1 and board[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, dist[i][j])

print(ans)
