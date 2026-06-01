def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s) 
    
    for step in range(1, len(s)//2+1):
        # 1. 쪼개기 
        tmp = ""
        prev = s[:step]
        count = 1
    
        # 2. 같은 문자열인지 확인하기 
        for i in range(step, len(s), step):
            curr = s[i:i+step]
            
            # 3. 같으면 축약, 다르면 그냥 추가 
            if prev == curr:
                count += 1
            else:
                tmp += (str(count) if count > 1 else "") + prev
                prev = curr
                count = 1
    
        tmp += (str(count) if count > 1 else "") + prev
        answer = min(answer, len(tmp))
  
    return answer
    