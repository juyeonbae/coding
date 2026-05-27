from collections import deque

def solution(maps):
    answer = []
    
    q = deque([])
    n, m = len(maps), len(maps[0])
    maps = [list(row.strip()) for row in maps]
    
    # 방문 체크 
    visited = [[False] * m for _ in range(n)]
           
    def bfs(sx, sy):
        q.append((sx, sy))
        total = int(maps[sx][sy])
        
        while q:
            x, y = q.popleft()

            for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]: 
                    visited[nx][ny] = True
                    total += int(maps[nx][ny])
                    q.append((nx, ny))
                    
        return total
    
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j].isdigit():
                visited[i][j] = True
                cnt = bfs(i, j)
                answer.append(cnt)
    
    if answer:
        answer.sort()
        return answer
    else: return [-1]