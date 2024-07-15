# 리스트 사용 
from collections import Counter

def solution(participant, completion):
    answer = ''
    par = Counter(participant)
    com = Counter(completion)

    par.subtract(com)

    for p in par:
        if par[p] > 0:
            answer = p
            break

    return answer

# 딕셔너리 사용 
def solution(participant, completion):
    answer, par = '', {}
    for p in participant:
        if p in par:
            par[p] += 1
        else:
            par[p] = 1

    for c in completion:
        if c in par:
            par[c] -= 1
            if par[c] == 0:
                del par[c]

    for key in par:
        answer = key

    return answer
