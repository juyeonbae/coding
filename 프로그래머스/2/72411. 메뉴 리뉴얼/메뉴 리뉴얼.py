from itertools import combinations

def solution(orders, course):
    answer = []
    orders = [list(o) for o in orders]
    
    for c in course:
        d = {}
        for order in orders:
            for comb in combinations(order, c):
                tmp = ''.join(sorted(comb))
                d[tmp] = d.get(tmp, 0) + 1
        
        if not d:
            continue
            
        mx = max(d.values())
        
        if mx < 2:
            continue 
            
        for k, v in d.items():
            if v == mx:
                answer.append(k)
                    
    return sorted(answer)