def solution(participant, completion):
    answer = ''
    
    d = {}
    for p in participant:
        if p in d:
            d[p] += 1 
        else:
            d[p] = 1
    
    for c in completion:
        if c in d:
            d[c] -= 1
    
    for k, v in d.items():
        if v == 1:
            answer = k
    return answer