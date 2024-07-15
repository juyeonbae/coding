############# 첫번째 풀이 ################

from itertools import combinations as c

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    lst = list(c(arr, i))

    for j in lst:
        tmp = sum(j)
        if tmp == S:
            cnt += 1

print(cnt)

############## 두번째 풀이 ################

from itertools import combinations

def subset_sums(arr):
    sums = []
    n = len(arr)
    for i in range(n + 1):
        for comb in combinations(arr, i):
            sums.append(sum(comb))
    return sums

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 배열을 두 부분으로 나누기
mid = N // 2
left = arr[:mid]
right = arr[mid:]

# 두 부분에 대한 부분 집합의 합 계산
left_sums = subset_sums(left)
right_sums = subset_sums(right)

# 두 부분 집합의 합이 S가 되는 경우 찾기
cnt = 0
right_sums_dict = {}
for s in right_sums:
    if s in right_sums_dict:
        right_sums_dict[s] += 1
    else:
        right_sums_dict[s] = 1

for s in left_sums:
    target = S - s
    if target in right_sums_dict:
        cnt += right_sums_dict[target]

# S가 0인 경우는 공집합을 제외해야 함
if S == 0:
    cnt -= 1

print(cnt)


'''
left = -7, -3
right = -2, 5, 8

left_sums = 1(-7, -3), 2(-10) 
right_sums = 1(-2,5,8) 2(3,6) 3(11)

d = {-2:1, 5:1, 8:1, 3:1, 6:1, 11:1}

target = 7, 3, 10 

target in dict => cnt += 1 

'''