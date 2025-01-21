S, K = map(int, input().split())

ans = 1
while S > 0:
    x = S / K
    x = round(x)
    S -= x
    K -= 1
    ans *= x

print(ans)