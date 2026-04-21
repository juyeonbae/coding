def solution(k, m, score):
    answer = 0
    # 상자 가격 = 가장 낮은 점수 * m개 
    score.sort(reverse=True)
    for i in range(m-1, len(score), m):
        answer += score[i] * m
    return answer