n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
s, e = arr[0][0], arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0] >= e:
        cnt += 1
        s, e = arr[i][0], arr[i][1]

print(cnt)