def solution(ms):
    answer = []
    for i in range(len(ms)):
        answer.append(ms[i:]) 
    return sorted(answer)
