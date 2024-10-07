T = int(input()) 

def fcnt(n):
    dp_zero = [0] * (n + 1)  # f(0)의 호출 횟수
    dp_one = [0] * (n + 1)   # f(1)의 호출 횟수

    if n >= 0:
        dp_zero[0] = 1  # f(0)이 호출되는 경우
    if n >= 1:
        dp_one[1] = 1   # f(1)이 호출되는 경우

    for i in range(2, n + 1):
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]

    return dp_zero[n], dp_one[n]

for _ in range(T):
    n = int(input())
    zero_count, one_count = fcnt(n)
    print(zero_count, one_count)
