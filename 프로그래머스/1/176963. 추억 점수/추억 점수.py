def solution(name, yearning, photo):
    answer, d = [], {}

    for i in range(len(name)):
        d[name[i]] = yearning[i]

    for p in photo:
        tmp = 0
        for i in p:
            if i in d:
                tmp += d[i]
        answer.append(tmp)

    return answer