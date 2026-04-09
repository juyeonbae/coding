import sys
input = sys.stdin.readline

MOD = 1000000007

def mat_mul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0:
                continue
            for j in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def mat_pow(M, p):
    n = len(M)
    # 단위행렬
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while p:
        if p & 1:
            result = mat_mul(result, M)
        M = mat_mul(M, M)
        p >>= 1
    return result

n = int(input())
ans2 = (n - 2) % MOD

base = [[1, 1], [1, 0]]
result = mat_pow(base, n)
ans1 = result[0][1]  # fib(n)

print(ans1, ans2)