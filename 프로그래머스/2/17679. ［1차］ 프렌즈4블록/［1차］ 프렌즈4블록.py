def solution(m, n, board):
    answer = 0
    board =  [list(row) for row in board]
    
    while True:
        # 1. 2x2 블록 찾기 
        remov = set() 
        
        for i in range(m-1):
            for j in range(n-1):
                chk = board[i][j] 
                
                if chk == '.': continue
                if (board[i][j+1] == chk and 
                   board[i+1][j] == chk and
                   board[i+1][j+1] == chk):
                    remov.add((i, j))
                    remov.add((i+1, j))
                    remov.add((i, j+1))
                    remov.add((i+1, j+1))

        if not remov: break 
        
        # 2. 찾은 블록들 제거 
        answer += len(remov)
        
        for x, y in remov:
            board[x][y] = '.'

        # 3. 제거되면 위의 값들 당기기 
        for j in range(n):
            tmp = []
            
            # 3-1. 아래에서 위로 보면서 살아있는 블록만 모음 
            for i in range(m-1, -1, -1):
                if board[i][j] != '.':
                    tmp.append(board[i][j])
                    
            # 3-2. 아래부터 다시 채우기 
            empty_count = m - len(tmp)
            col = ['.'] * empty_count + tmp[::-1] 
            
            for i in range(m):
                board[i][j] = col[i]
            
    return answer