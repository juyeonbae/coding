def solution(n):
    if n == 0:
        return "0"
        
    ans = ''
    
    while n:
        remainder = n % 3
        n = n // 3
        
        if remainder == 2 or remainder == -2:
            n += 1
            ans = '-' + ans
        elif remainder == -1:
            ans = '-' + ans
        else:
            ans = str(remainder) + ans
            
    return ans

T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))