n = int(input())
arr = list(map(int, input().split()))

arr.sort()
t, mn = 0, 0
for i in range(len(arr)):
    t = t + arr[i]
    mn += t

print(mn)