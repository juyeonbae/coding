import sys
input = sys.stdin.readline
from collections import deque

# 0 빈공간, X 벽, I 도연, P 사람
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            x, y = i, j

        if arr[i][j] == 'X':
            visited[i][j] = True

q = deque([(x, y)])
visited[x][y] = True 
cnt = 0 

while q:
    x, y = q.popleft()

    for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True
            if arr[nx][ny] == 'P':
                cnt += 1

print(cnt if cnt else 'TT')