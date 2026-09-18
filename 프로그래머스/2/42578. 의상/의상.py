def solution(clothes):
    d = {}
    for n, k in clothes:
        if k in d:
            d[k].append(n)
        else:
            d[k] = [n]
    
    s = 1
    for k, v in d.items():
        s *= len(v) + 1
        
    return s-1