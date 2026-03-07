import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
count = 0

for right in range(n):
    # 1. right를 한 칸 늘리면서 현재 구간 합에 포함
    curr_sum += arr[right]

    # 2. 합이 m보다 크면 left를 움직여서 줄임
    while curr_sum > m:
        curr_sum -= arr[left]
        left += 1

    # 3. 합이 m이면 경우의 수 1개 추가
    if curr_sum == m:
        count += 1

print(count)