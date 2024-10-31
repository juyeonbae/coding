n, k = map(int,input().split())
arr = list(map(int,input().split()))

lst = []
tmp = sum(arr[:k])
lst.append(tmp)

for i in range(1,n-k+1):
    tmp += arr[i+k-1] - arr[i-1]
    lst.append(tmp)

print(max(lst))