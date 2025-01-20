import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

xor_sum = 0
for num in nums:
    xor_sum ^= num

answer = xor_sum
for num in nums:
    temp = xor_sum ^ num
    answer = max(answer, temp)

print(str(answer) * 2)