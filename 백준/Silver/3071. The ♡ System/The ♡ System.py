def solution(n):
    if n == 0: return "0"

    ans = ''
    while n:
        r = n % 3
        n = n // 3

        if abs(r) == 2 or r == -1:
            if abs(r) == 2: n += 1
            ans += '-'
        else:
            ans += str(r)

    return ans[::-1]


T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))