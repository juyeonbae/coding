def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


T = int(input())
for _ in range(T):
    A, B, X = map(int, input().split())

    num = gcd(A, B)
    answer = X // num

    print(answer)