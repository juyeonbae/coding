def solution(bandage, health, attacks):
    answer = health

    # t초 기준으로 반복
    t = 0
    a = 0  # 공격 시간
    cnt = 0  # 연속 성공
    fin = attacks[-1][0]  # 마지막 공격 시간
    while True:
        if t == fin + 1:
            break

        # 공격
        if t == attacks[a][0]:
            answer -= attacks[a][1]
            a += 1
            cnt = 0

            # 공격으로 죽었는지 확인
            if answer <= 0:
                return -1

        # 기술 시전
        else:
            answer += bandage[1]  # 1초당 체력 회복
            cnt += 1

            # 연속 성공 = t초 -> 추가 회복
            if cnt == bandage[0]:
                answer += bandage[2]
                cnt = 0

            # 최대 체력 초과 시
            if answer >= health:
                answer = health

        t += 1

    return answer