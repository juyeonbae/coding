def solution(video_len, pos, op_start, op_end, commands):
    # 비디오 길이
    v_mm, v_ss = map(int, video_len.split(":"))

    # 현재 위치
    cur_mm, cur_ss = map(int, pos.split(":"))

    # 오프닝 위치
    ops_mm, ops_ss = map(int, op_start.split(":"))
    ope_mm, ope_ss = map(int, op_end.split(":"))

    for c in commands:
        # 현재 위치가 op구간일 때 next 입력 시 op_end로 이동
        if (ops_mm * 60 + ops_ss) <= (cur_mm * 60 + cur_ss) <= (ope_mm * 60 + ope_ss):
            cur_mm, cur_ss = ope_mm, ope_ss

        # prev - 10초 전으로 이동
        if c == 'prev':
            # cur_ss >= 10 일 때
            if cur_ss >= 10:
                cur_ss -= 10

            # cur_ss < 10 일 때 (10초 미만일 때/cur_mm 있는 경우)
            elif cur_mm == 0 and cur_ss <= 10:
                cur_mm, cur_ss = 0, 0

            else:
                cur_mm -= 1
                cur_ss += 50  # 60초에서 10초 빼고 더하기

        # next - 10초 후로 이동
        elif c == 'next':
            # 동영상이 10초도 안 남았을 때
            if (v_mm * 60 + v_ss) <= cur_mm * 60 + cur_ss + 10:
                cur_mm, cur_ss = v_mm, v_ss

            else:
                cur_ss += 10
                if cur_ss >= 60:
                    cur_mm += cur_ss//60
                    cur_ss %= 60

        # 마지막 명령 후에도 다시 오프닝 구간 건너뛰기
        if (ops_mm * 60 + ops_ss) <= (cur_mm * 60 + cur_ss) <= (ope_mm * 60 + ope_ss):
            cur_mm, cur_ss = ope_mm, ope_ss

    if cur_mm < 10: mm = '0' + str(cur_mm)
    else: mm = str(cur_mm)

    if cur_ss < 10: ss = '0' + str(cur_ss)
    else: ss = str(cur_ss)

    return mm + ":" + ss