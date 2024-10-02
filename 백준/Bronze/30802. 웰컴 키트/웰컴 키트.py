import math

N = int(input())
shirt_requests = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 최소 묶음 수 계산
shirt = 0
for i in range(len(shirt_requests)):
    shirt += math.ceil(shirt_requests[i] / T)

pen_bundles, pen = sum(shirt_requests)//P, sum(shirt_requests) % P

print(shirt)
print(pen_bundles, pen)

