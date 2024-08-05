from collections import deque

def solution(answers):
    answer = []

    one = deque([1,2,3,4,5])
    two = deque([2,1,2,3,2,4,2,5])
    three = deque([3,3,1,1,2,2,4,4,5,5])

    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == one[0]:
            cnt1 += 1
        one.rotate(-1)

        if answers[i] == two[0]:
            cnt2 += 1
        two.rotate(-1)

        if answers[i] == three[0]:
            cnt3 += 1
        three.rotate(-1)

    # 비교를 어떻게 하지?
    arr = [0, cnt1, cnt2, cnt3]

    max_cnt = max(arr)
    for i in range(1, len(arr)):
        if max_cnt == arr[i]:
            answer.append(i)

    return answer