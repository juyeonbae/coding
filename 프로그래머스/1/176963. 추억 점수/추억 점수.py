def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))
    
    for p in photo:
        tmp = 0
        for i in p:
            if i in d:
                tmp += d[i]
        answer.append(tmp)

    return answer