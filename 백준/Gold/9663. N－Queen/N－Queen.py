import sys
input = sys.stdin.readline

n = int(input())

visited = [False] * n
diag_down = [False] * (2 * n - 1) # / 방향
diag_up = [False] * (2 * n - 1) # \ 방향


def backtrack(row):
    # 종료 조건 
    if row == n:
        return 1

    total = 0 

    # for 선택지 in 가능한 후보들: 
    for col in range(n):
        d_down = row - col + (n-1)
        d_up = row + col

        if visited[col] or diag_down[d_down] or diag_up[d_up]:
            continue
            
        # 선택할 수 있다면 선택 
        visited[col] = True
        diag_down[d_down] = True
        diag_up[d_up] = True

        total += backtrack(row+1)
        
        # 선택 취소
        visited[col] = False
        diag_down[d_down] = False
        diag_up[d_up] = False

    return total

print(backtrack(0))
        