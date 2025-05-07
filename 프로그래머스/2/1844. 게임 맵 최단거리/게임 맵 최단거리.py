from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    
    q.append((0, 0))
    visited[0][0] = True
    dist[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    print(dist)
    return dist[n-1][m-1]