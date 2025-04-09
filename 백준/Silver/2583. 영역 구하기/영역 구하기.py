from collections import deque

n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(y1, y2):
        for k in range(x1, x2):
            grid[j][k] = 1

q = deque()
ans = []

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and not grid[x][y] 

    
def bfs(x, y):
    cnt = 1
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1 

    ans.append(cnt)
                
    
for i in range(n):
    for j in range(m):
        if not grid[i][j] and not visited[i][j]:
            bfs(i, j)

print(len(ans))
ans.sort()
print(*ans)
