from itertools import permutations as p

def solution(k, dungeons):
    mx_cnt = 0
    lst = list(p(dungeons, len(dungeons)))  # 던전의 수만큼 모든 순열 리스트 
    
    for tc in lst:
        hp = k  # 체력
        cnt = 0  # 던전 수
        
        for minimum, consume in tc:
            if hp < minimum:
                break
            else:
                cnt += 1 
                hp -= consume
        
        if mx_cnt < cnt:
            mx_cnt = cnt
            
    return mx_cnt