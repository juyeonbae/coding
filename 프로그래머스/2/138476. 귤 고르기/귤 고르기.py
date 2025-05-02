def solution(k, tangerine):
    answer, dct = 0, {}
    for t in tangerine:
        if t in dct:
            dct[t] += 1
        else:
            dct[t] = 1
            
    dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    
    chk = 0 
    for num, v in dct:    
        if chk >= k:
            break
        else:
            chk += v 
            answer += 1
        
    return answer
