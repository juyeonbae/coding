import sys
input = sys.stdin.readline

N = int(input())
nums = []
total = 0  # 합계를 위한 변수
freq_dict = {}  # 빈도수 계산을 위한 딕셔너리

# 입력받으면서 동시에 합계와 빈도수 계산
for _ in range(N):
    num = int(input())
    nums.append(num)
    total += num
    freq_dict[num] = freq_dict.get(num, 0) + 1

nums.sort()  # 한 번의 정렬

# 산술평균
print(round(total/N))

# 중앙값
print(nums[N//2])

# 최빈값 
max_freq = max(freq_dict.values())
mode_vals = sorted([num for num, freq in freq_dict.items() if freq == max_freq])
print(mode_vals[1] if len(mode_vals) > 1 else mode_vals[0])

# 범위
print(nums[-1] - nums[0])