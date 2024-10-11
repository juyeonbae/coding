def solution(citations):
    answer = 0
    citations.sort()
    max_check = 0
    for h in range(max(citations)+1):
        cnt = 0
        for idx in range(len(citations)):
            if h <= citations[idx]:
                cnt += 1
            if cnt == h:
                answer = cnt
                max_check = max(max_check,answer)
    # 테케 11번이 뭐지?
    return max_check