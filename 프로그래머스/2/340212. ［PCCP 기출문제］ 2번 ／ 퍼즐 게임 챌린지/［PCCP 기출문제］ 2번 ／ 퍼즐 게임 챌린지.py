def solution(diffs, times, limit):
    left, right = 1, max(diffs)  # 숙련도의 범위를 1에서 최대 난이도 값까지 설정

    while left < right:
        mid = (left + right) // 2
        total_time = 0

        for i in range(len(diffs)):
            # 퍼즐 난이도 > mid (현재 숙련도)
            if diffs[i] > mid:
                total_time += (diffs[i] - mid) * (times[i] + times[i-1]) + times[i]
            else:
                total_time += times[i]

        # 퍼즐 다 푸는 시간이 limit 이하일 때
        if total_time <= limit:
            right = mid  # 가능한 더 낮은 level 찾기
        else:
            left = mid + 1  # 숙련도 부족, level을 높임

    return left  # 최소한의 level
