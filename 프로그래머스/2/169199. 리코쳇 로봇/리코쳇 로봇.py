from collections import deque

def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    
    q = deque([])
    dist = [[-1] * m for _ in range(n)] 
    
    fx, fy = 0, 0
    
    board = [list(b) for b in board]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j))
                dist[i][j] = 0 
            
            if board[i][j] == 'G':
                fx, fy = i, j
    
    while q:
        x, y = q.popleft()
        
        
        for dx, dy in ([-1, 0], [0, 1], [1, 0], [0, -1]):
            nx, ny = x, y
            
            while True:
                tx, ty = nx + dx, ny + dy
                if not (0 <= tx < n and 0 <= ty < m):
                    break
                if board[tx][ty] == 'D':
                    break

                nx, ny = tx, ty
        
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist[fx][fy]