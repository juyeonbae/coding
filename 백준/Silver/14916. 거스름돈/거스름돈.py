import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
i = n//5

if n == 1 or n == 3:
    print(-1)
else:
    cnt = n // 5
    remainder = n % 5

    if remainder % 2 != 0:
        cnt -= 1
        remainder += 5

    cnt += remainder // 2
    print(cnt)
