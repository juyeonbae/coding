def count(n, limit, power):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i == n//i:
                cnt += 1
            else:
                cnt += 2

    if cnt > limit:
        return power
    return cnt


def solution(number, limit, power):
    # 1. 약수의 개수 구하기
    arr = []
    for i in range(1, number+1):
        x = count(i, limit, power)
        arr.append(x)

    return sum(arr)