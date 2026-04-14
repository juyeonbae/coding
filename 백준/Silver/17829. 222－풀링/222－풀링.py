import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = float('-inf')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dv(r, c, size):
    if size == 2:
        pool = []
        for i in range(r, r+2):
            for j in range(c, c+2):
                pool.append(arr[i][j])
            pool.sort(reverse=True)
        return pool[1] 

    # 1. 분할
    half = size // 2
    res = [
        dv(r, c, half), # 왼쪽 위
        dv(r, c+half, half), # 오른쪽 위
        dv(r+half, c, half), # 왼쪽 아래
        dv(r+half, c+half, half) # 오른쪽 아래 
    ]

    # 2. 합치기
    res.sort(reverse=True)
    return res[1]

print(dv(0, 0, n))
    