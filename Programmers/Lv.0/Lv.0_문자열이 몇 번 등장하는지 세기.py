def solution(ms, p):
    answer = 0
    for i in range(len(ms)):
        if ms[i:i+len(p)] == p[:]:
            answer += 1
    return answer
