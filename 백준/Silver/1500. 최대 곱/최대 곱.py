S, K = map(int, input().split())

ans = 1
for _ in range(K):
    x = round(S / (K - _))
    ans *= x
    S -= x

print(ans)