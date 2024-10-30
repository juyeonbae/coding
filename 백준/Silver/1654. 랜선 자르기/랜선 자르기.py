k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

# 이분 탐색 범위 설정
start = 1
end = max(arr)

# 이분 탐색 수행
result = 0
while start <= end:
    mid = (start + end) // 2  # 현재 길이 설정
    cnt = sum(x // mid for x in arr)  # 막대를 현재 길이로 잘라 얻을 수 있는 개수

    if cnt >= n:
        # 길이를 늘려서 더 큰 길이를 시도
        result = mid
        start = mid + 1
    else:
        # 길이를 줄여서 시도
        end = mid - 1

print(result)
