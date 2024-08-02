def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]

    zero = lottos.count(0)
    
    cnt = 0
    for i in win_nums:
        if i in lottos:
            cnt += 1

    return answer[zero + cnt], answer[cnt]
