from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

q = deque()

def can_go(x, y, visited):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]


def bfs(i, j, txt, arr, visited):
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, visited) and arr[nx][ny] == txt:
                q.append((nx, ny))
                visited[nx][ny] = True


tmp = [[''] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] in ['R', 'G']:
            tmp[i][j] = 'R'
        else:
            tmp[i][j] = 'B'

a, b = 0, 0  # 적록색약 X / 적록색약 O
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            txt = grid[i][j]
            bfs(i, j, txt, grid, visited1)
            a += 1
        if not visited2[i][j]:
            txt = tmp[i][j]
            bfs(i, j, txt, tmp, visited2)
            b += 1

print(a, b)