from itertools import combinations_with_replacement

N = int(input())
values = [1, 5, 10, 50]

# 중복을 허용하여 N개를 뽑는 모든 조합을 구함
combos = combinations_with_replacement(values, N)

# 각 조합의 합을 구한 뒤 set으로 중복 제거
answer = set(sum(c) for c in combos)

print(len(answer))