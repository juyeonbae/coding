def solution(genres, plays):
    dct = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dct:
            dct[g] = []
        dct[g].append([i, p])
    # {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}

    # 각 장르의 리스트를 재생 수(play) 기준으로 내림차순 정렬
    for g in dct:
        dct[g].sort(key=lambda x:x[1], reverse=True)

    # 장르를 총 재생 수 합계 기준으로 내림차순 정렬
    dct = dict(sorted(dct.items(), key=lambda x: sum(p for _, p in x[1]), reverse=True))
    print(dct)

    answer = []
    for g in dct.values():
        print(g)
        if len(g) == 1:
            answer.append(g[0][0])
        else:
            for i in range(2):
                answer.append(g[i][0])

    return answer