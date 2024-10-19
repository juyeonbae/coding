def solution(n):
    cnt = 0
    # 시작점(start)을 1부터 n까지 움직이면서 처리
    for start in range(1, n + 1):
        tmp = 0
        # 시작점에서 출발하여 연속된 수들의 합을 계산
        for end in range(start, n + 1):
            tmp += end
            if tmp == n:
                cnt += 1
                break
            elif tmp > n:
                break

    return cnt