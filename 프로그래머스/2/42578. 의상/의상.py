def solution(clothes):
    dct = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dct:
            dct[clothes[i][1]] += 1
        else:
            dct[clothes[i][1]] = 1

    answer = 1
    for i in dct.keys():
        answer *= (dct[i] + 1)

    return answer - 1