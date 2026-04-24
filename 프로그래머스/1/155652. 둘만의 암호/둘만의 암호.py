def solution(s, skip, index):
    answer = ''
    # index만큼 뒤의 알파벳으로 바꿈  
    # index만큼의 뒤의 알파벳이 z를 넘어가면 a로 
    # skip에 있는 알파벳은 제외하고 건너뜀
    
    for i in range(len(s)):
        x = 0
        k = 1
        while x < index:
            tmp = chr((ord(s[i]) - ord('a') + k) % 26 + ord('a'))
            if tmp in skip:
                k += 1
                continue
            
            k += 1
            x += 1
            
        answer += tmp                
            
    return answer