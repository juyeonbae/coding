import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

xor_all = 0
for num in nums:
    xor_all ^= num

print(str(max(xor_all, max(xor_all ^ num for num in nums))) * 2)