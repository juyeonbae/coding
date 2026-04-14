import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000

n, b = map(int, input().split())
A = [(list(map(int, input().split()))) for _ in range(n)]

# 행렬 곱셈
def mul(A, B, MOD):
    n = len(A)
    arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr[i][j] = (arr[i][j] + A[i][k] * B[k][j]) % MOD 

    return arr


# 거듭 제곱 - 분할정복
def power(A, B, MOD):
    if B == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= MOD
        return A

    # 1. 분할 
    half = power(A, B//2, MOD)

    # 2. 합치기
    if B % 2 == 0: 
        return mul(half, half, MOD)
    else: 
        return mul(mul(half, half, MOD), A, MOD)


answer = power(A, b, MOD)

for row in answer:
    print(*row)