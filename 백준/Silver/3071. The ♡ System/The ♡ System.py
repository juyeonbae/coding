def solution(n):
    if n == 0:
        return "0"
        
    ans = ''
    is_negative = n < 0
    n = abs(n)
    
    while n:
        remainder = n % 3
        n = n // 3
        
        if remainder == 2:
            n += 1
            ans = '-' + ans
        else:
            ans = str(remainder) + ans
            
    if is_negative:
        # 음수인 경우 각 자리의 부호를 반전
        new_ans = ''
        for c in ans:
            if c == '1':
                new_ans += '-'
            elif c == '-':
                new_ans += '1'
            else:
                new_ans += '0'
        ans = new_ans
        
    return ans

T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))