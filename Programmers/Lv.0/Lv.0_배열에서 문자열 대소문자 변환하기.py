def solution(strArr):
    answer = []
    for s in range(len(strArr)):
        if s % 2 == 0:
            answer.append(strArr[s].lower())
        else:
            answer.append(strArr[s].upper())
    return answer
