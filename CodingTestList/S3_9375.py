T = int(input())
for tc in range(T):
    n = int(input())
    d = {}
    for i in range(n):
        cloth, ctype = input().split()
        if ctype in d:
            d[ctype] += 1
        else:
            d[ctype] = 1

    s = 1
    for key, value in d.items():
        s *= (value + 1)

    print(s - 1)
