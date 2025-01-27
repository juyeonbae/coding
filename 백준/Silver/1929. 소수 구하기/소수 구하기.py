N, M = map(int, input().split())

arr = [False, False] + [True] * (M-1)
primes = []

for i in range(2, M+1):
    if arr[i]:
        primes.append(i)
        for j in range(2*i, M+1, i):
            arr[j] = False

for p in primes:
    if p >= N:
        print(p)