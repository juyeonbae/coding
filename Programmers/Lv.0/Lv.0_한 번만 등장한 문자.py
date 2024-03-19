def solution(s):
    answer = ''
    for i in set(s):
        if s.count(i) == 1: answer += i
            
    return ''.join(sorted(answer))
