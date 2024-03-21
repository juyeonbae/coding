def solution(ms, q):
    for s,e in q:
        ms = ms[:s] + ms[s:e+1][::-1] + ms[e+1:]
    
    return ms
