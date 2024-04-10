n = int(input())

for i in range(n // 5, -1, -1):
    re = n - 5 * i
    if re % 3 == 0:
        print(i + re//3)
        break
else:
    for i in range(n//3, -1, -1):
        re = n - 3 * i
        if re % 5 == 0:
            print(i + re//5)
            break
    else:
        print(-1)
