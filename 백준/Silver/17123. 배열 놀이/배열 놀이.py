import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    diff = [[0]*(n+2) for _ in range(n+2)]
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())

        # 차분으로 누적합 한 번에 할 배열 만들기 1-index
        diff[r1][c1] += v
        diff[r2+1][c2+1] += v
        diff[r1][c2+1] -= v
        diff[r2+1][c1] -= v

    row = [0]*n
    col = [0]*n
    for i in range(1, n+1):
        for j in range(1, n+1):
            diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
            arr[i-1][j-1] += diff[i][j]

            # 행, 열 합 바로 구하기 
            val = arr[i-1][j-1]
            row[i-1] += val
            col[j-1] += val

    print(* row)
    print(* col)