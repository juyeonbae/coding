import sys
input = sys.stdin.readline

def cal(n):
    for i in range(n):
        sumN, x = i, i  #i 값을 그대로 쓰면 변경되기 때문에 x에 임시저장 
    
        while x>=1:  #각 자리 수의 합
            sumN += x % 10
            x //= 10

        if n == sumN:
            return i

    return 0

n = int(input())
print(cal(n))
