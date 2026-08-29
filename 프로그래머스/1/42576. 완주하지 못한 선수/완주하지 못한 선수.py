
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