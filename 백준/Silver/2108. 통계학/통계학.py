import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())

nums = []
for _ in range(N):
  num = int(input())
  nums.append(num)
  
nums.sort()
  
# 산술평균 -> 소수점 첫째자리에서 반올림 
print(round(sum(nums)/len(nums)))

# 중앙값
print(nums[len(nums)//2])

# 최빈값 -> 여러 개가 있을 경우 두 번째로 작은 값
print(Counter(nums).most_common()[1][0] if len(nums) > 1 and Counter(nums).most_common()[0][1] == Counter(nums).most_common()[1][1] else Counter(nums).most_common()[0][0])

# 범위 출력 
print(nums[-1] - nums[0])