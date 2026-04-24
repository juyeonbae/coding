def solution(s):
    answer = 0
    '''
    각 자리 숫자를 0으로 만든다.
    0~5는 내리고, 6~9는 올린다.
    처리한 자리는 버리고 다음 자리로 간다.
    '''
    while s > 0:
        digit = s % 10
        
        if digit < 5:
            s -= digit
            answer += digit
            
        elif digit > 5:
            answer += (10-digit)
            s += (10-digit)
            
        else:
            if (s // 10) % 10 >= 5:
                answer += 5
                s += 10 
            else:
                answer += 5
            
        s //= 10
    
    return answer