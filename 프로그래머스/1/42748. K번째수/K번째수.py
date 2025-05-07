def solution(array, commands):
    answer = []
    for s, e, target in commands:
        tmp = sorted(array[s-1: e])
        answer.append(tmp[target-1])
    return answer