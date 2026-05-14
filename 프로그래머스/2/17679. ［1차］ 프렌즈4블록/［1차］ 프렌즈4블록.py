def solution(m, n, board):
    answer = 0
    
    # 1. 2x2 블록 찾기 
    remov = set() 
    for i in range(m):
        for j in range(n):
            chk = board[i][j] 
            for dx, dy in ([0, 1], [1, 0], [1, 1]):
                nx, ny = i + dx, j + dy
                if 0 > nx or nx >= m or 0 or 0 > ny or ny >= n or board[nx][ny] != chk:
                    break
            else:
                remov.add((i, j))
                remov.add((i+1, j))
                remov.add((i, j+1))
                remov.add((i+1, j+1))
   
    print(remov)          
    # 2. 찾은 블록들 제거 
    answer += len(remov)
    for x, y in remov:
        board[x][y].replace(board[x][y], ".")
    
    print(board)
    # 3. 제거되면 위의 값들 당기기 
    for j in range(n):
        for i in range(m):
            if board[i][j] == '.':
                pass
    
    return answer