def solution(n, s):
    answer = []
    if s // n == 0: 
        return [-1]

    while n > 0:
        tmp = s // n 
        s -= tmp 
        n -= 1
        answer.append(tmp)
    
    return answer