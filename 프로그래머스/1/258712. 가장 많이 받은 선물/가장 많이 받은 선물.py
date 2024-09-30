def solution(friends, gifts):

    # 준 사람, 받은 사람 저장 어떻게 할 건지?
    arr = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for i in range(len(gifts)):
        A, B = gifts[i].split()
        x, y = friends.index(A), friends.index(B)
        arr[x][y] += 1

    # 선물 지수 계산 (gift_num)
    friends_dic = {f: 0 for f in friends}
    for i in range(len(arr)):
        friends_dic[friends[i]] += sum(arr[i])  # 행 합산
        friends_dic[friends[i]] -= sum(col[i] for col in arr)  # 열 합산


    # 다음 달 받을 선물 계산(friends_gift_num)
    friends_gift_num = {f: 0 for f in friends}
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j: continue  # 자기자신 제외

            # 1. 선물 교류가 있는 경우 > 선물 개수 비교
            elif i != j and (arr[i][j] != 0 or arr[j][i] != 0):
                if arr[i][j] > arr[j][i]:
                    friends_gift_num[friends[i]] += 1
                elif arr[i][j] < arr[j][i]:
                    friends_gift_num[friends[j]] += 1

                # 1-1. 차이가 없으면 선물 지수 비교
                elif arr[i][j] == arr[j][i]:
                    if friends_dic[friends[i]] > friends_dic[friends[j]]:
                        friends_gift_num[friends[i]] += 1
                    elif friends_dic[friends[i]] < friends_dic[friends[j]]:
                        friends_gift_num[friends[j]] += 1

            # 2. 선물 교류가 없는 경우 > 선물 지수 비교
            else:
                if friends_dic[friends[i]] > friends_dic[friends[j]]:
                    friends_gift_num[friends[i]] += 1
                elif friends_dic[friends[i]] < friends_dic[friends[j]]:
                    friends_gift_num[friends[j]] += 1

    # 선물 많이 받은 사람 추출
    res = []
    for k,v in friends_gift_num.items():
        res.append(v//2)

    answer = max(res)

    return answer