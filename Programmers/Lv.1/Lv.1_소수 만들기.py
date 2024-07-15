from itertools import combinations as combi

# 소수 판별 함수 
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

# main 
def solution(nums):
    arr, cnt = list(combi(nums, 3)), 0

    for i in arr:
        tmp = sum(i)
        if isPrime(tmp):
            cnt += 1

    return cnt
