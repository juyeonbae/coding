import math

def solve(n):
    # 1. 완전제곱수인 경우
    if int(math.sqrt(n)) ** 2 == n:
        return 1
    
    # 2. 두 제곱수의 합으로 표현되는 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        remaining = n - i*i
        if int(math.sqrt(remaining)) ** 2 == remaining:
            return 2
            
    # 3. 세 제곱수의 합으로 표현되는 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i*i)) + 1):
            remaining = n - i*i - j*j
            if int(math.sqrt(remaining)) ** 2 == remaining:
                return 3
    
    # 4. 나머지는 모두 4개의 제곱수로 표현 가능
    return 4

n = int(input())
print(solve(n))