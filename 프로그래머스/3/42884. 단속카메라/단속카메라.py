def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    
    x = -30001
    for s, e in routes:
        if s <= x <= e:
            continue
        else:
            x = e 
            answer += 1
            
    return answer