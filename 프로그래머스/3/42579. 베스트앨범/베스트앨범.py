def solution(genres, plays):
    # 딕셔너리 생성 및 장르별 재생 기록 추가
    dct = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        dct.setdefault(g, []).append([i, p])

    # 각 장르의 리스트를 재생 수 기준으로 내림차순 정렬
    for g in dct:
        dct[g].sort(key=lambda x: x[1], reverse=True)

    # 장르별 총 재생 수를 기준으로 딕셔너리 자체도 내림차순 정렬
    dct = dict(sorted(dct.items(), key=lambda x: sum(p for _, p in x[1]), reverse=True))

    # 최대 두 곡씩 인덱스를 추출
    return [i for g in dct.values() for i, _ in g[:2]]
