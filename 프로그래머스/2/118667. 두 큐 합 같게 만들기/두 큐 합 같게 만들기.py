from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    cnt = 0 
    q1sum, q2sum = sum(q1), sum(q2)
    limit = len(q1) * 3
    
    if (q1sum + q2sum) % 2 == 1:
        return -1 
    
    while cnt <= limit:
        if q1sum == q2sum:
            return cnt 
            
        if q1sum > q2sum:
            tmp = q1.popleft() 
            q2.append(tmp)
            q1sum -= tmp
            q2sum += tmp 
            cnt += 1
            
        elif q1sum < q2sum:
            tmp = q2.popleft()
            q1.append(tmp)
            q1sum += tmp
            q2sum -= tmp 
            cnt += 1
            
    return -1 