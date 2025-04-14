from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

def bfs(color_blind):
    visited = [[False] * n for _ in range(n)]
    area = 0
    q = deque()

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                area += 1
                visited[i][j] = True
                cur_color = grid[i][j] 
                q.append((i, j)) 
       
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            next_color = grid[nx][ny]
                            if color_blind and (cur_color in ['R', 'G'] and next_color in ['R', 'G']) or (cur_color == next_color):
                                visited[nx][ny] = True 
                                q.append((nx, ny))
                            elif not color_blind and cur_color == next_color:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    
    return area


normal = bfs(color_blind=False)
blind = bfs(color_blind=True)

print(normal, blind)