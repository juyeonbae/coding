import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())  
nums = [int(input()) for _ in range(N)]  
nums.sort()

# 산술평균 (소수점 첫째 자리에서 반올림)
print(round(sum(nums) / N))

# 중앙값
print(nums[N // 2])

# 최빈값 찾기
counter = Counter(nums).most_common()  # 빈도수 내림차순 정렬
max_count = counter[0][1]  # 최빈값의 빈도수

# 빈도수가 가장 높은 값들만 필터링
modes = [num for num, count in counter if count == max_count]

# 최빈값 -> 여러 개가 있을 경우 두 번째로 작은 값 선택
print(modes[1] if len(modes) > 1 else modes[0])

# 범위 출력
print(nums[-1] - nums[0])
