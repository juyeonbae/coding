import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

asc_cnt, dsc_cnt = 1, 1
max_length = 1

for i in range(n-1):
    if arr[i] <= arr[i+1]: asc_cnt += 1
    else: asc_cnt = 1 

    if arr[i] >= arr[i+1]: dsc_cnt += 1
    else: dsc_cnt = 1

    max_length = max(max_length, asc_cnt, dsc_cnt)

print(max_length)