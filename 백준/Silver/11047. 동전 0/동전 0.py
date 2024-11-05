n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort(reverse=True)

cnt = 0
for i in range(len(arr)):
    cnt += k // arr[i]
    k %= arr[i]

print(cnt)
