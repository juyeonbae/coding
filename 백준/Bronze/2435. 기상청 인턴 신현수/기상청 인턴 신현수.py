n, k = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0]*(n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i-1]

ans = psum[k] - psum[0]
for i in range(k, n+1):
    x = psum[i] - psum[i-k]
    if x > ans:
        ans = x

print(ans)