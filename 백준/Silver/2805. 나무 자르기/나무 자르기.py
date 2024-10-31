n, m = map(int, input().split())  # 나무 수, 나무의 길이
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2 
    tree = sum(x-mid for x in arr if (x-mid) >= 0)

    if tree >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
