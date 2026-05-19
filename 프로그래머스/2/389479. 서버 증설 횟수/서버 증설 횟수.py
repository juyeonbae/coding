def solution(players, m, k):
    answer = 0  # 서버 증설 횟수 
    
    # 증설된 서버의 수 
    server = [0] * len(players) 
    
    # 증설된 서버가 언제까지 유효한 지 
    
    for idx, p in enumerate(players):
        tmp = server[idx]
        if p >= m: 
            s = p // m 
            if s <= tmp:
                continue
                
            else:
                answer += s-tmp
                r = idx+k if idx+k < len(players) else len(players)
                for i in range(idx, r):
                    server[i] += s-tmp
    
    return answer