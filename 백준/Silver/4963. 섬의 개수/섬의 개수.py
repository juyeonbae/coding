from collections import deque


def in_range(x, y):
    return 0 <= x < h and 0 <= y < w


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and arr[x][y] == 1


def bfs(x, y):
    dxs, dys = [1, 0, -1, 0, 1, 1, -1, -1], [0, 1, 0, -1, 1, -1, 1, -1]
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = True
                bfs(i, j)
                cnt += 1

    print(cnt)

