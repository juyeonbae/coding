import sys
input = sys.stdin.readline

n = int(input())

visited = [False] * n
diag_down = [False] * (2 * n - 1) # / 방향
diag_up = [False] * (2 * n - 1) # \ 방향


def count_queens(row):
    if row == n:
        return 1

    total = 0 

    for col in range(n):
        d_down = row - col + (n-1)
        d_up = row + col

        if visited[col] or diag_down[d_down] or diag_up[d_up]:
            continue

        visited[col] = True
        diag_down[d_down] = True
        diag_up[d_up] = True

        total += count_queens(row+1)

        visited[col] = False
        diag_down[d_down] = False
        diag_up[d_up] = False

    return total

print(count_queens(0))
        