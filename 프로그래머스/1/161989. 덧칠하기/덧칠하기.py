def solution(n, m, section):
    answer = 0
    last_point = 0
    
    for i in section:
        if i <= last_point:
            continue
        last_point = i + m - 1
        answer += 1
        
    return answer