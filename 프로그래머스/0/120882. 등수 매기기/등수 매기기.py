def solution(score):
    answer = [0] * len(score)

    arr = []
    for idx, s in enumerate(score):
        arr.append([idx, sum(s) / 2])

    arr.sort(key=lambda x: x[1], reverse=True)

    rank = 1
    mx = arr[0][1]
    cnt = 0

    for idx, sc in arr:
        if sc == mx:
            answer[idx] = rank
            cnt += 1
        else:
            rank += cnt
            answer[idx] = rank
            mx = sc
            cnt = 1

    return answer