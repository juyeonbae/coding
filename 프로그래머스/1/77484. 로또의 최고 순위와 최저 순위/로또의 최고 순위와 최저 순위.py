def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]

    zero, cnt, arr = 0, 0, []
    for i in lottos:
        if i == 0:
            zero += 1
        else:
            arr.append(i)

    for i in arr:
        for j in win_nums:
            if i == j:
                cnt += 1

    return answer[zero + cnt], answer[cnt]