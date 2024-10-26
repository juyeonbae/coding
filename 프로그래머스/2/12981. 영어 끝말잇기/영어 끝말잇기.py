def solution(n, words):
    dct = {i: [] for i in range(n)}

    cnt, rank = 0, 1
    for i in range(len(words)):
        d = i % n
        if i == 0:
            dct[d].append(words[i])
        else:
            w1, w2 = words[i-1], words[i]
            if len(w2) <= 1 or w1[-1] != w2[0] or any(words[i] in lst for lst in dct.values()):
                return [d+1, rank]

            else:
                dct[d].append(words[i])

        cnt += 1
        if cnt == n:
            rank += 1
            cnt = 0

    return [0,0]