def solution(ms, p):
    answer = []
    for i in range(len(ms)):
        if ms[i] == p[-1]:
            answer.append(ms[:i+1])
    return answer[-1]

#차례대로 answer에 추가할 것이므로, answer의 맨뒤 원소가 가장 길 것이다. 
