# S3_9461_파도반 수열.py

def padovan(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 3:
        memo[n] = 1
    else:
        memo[n] = padovan(n - 2) + padovan(n - 3)

    return memo[n]


T = int(input())  # testcase
for tc in range(T):
    n = int(input())
    memo = [-1 for _ in range(n+1)]
    print(padovan(n))
