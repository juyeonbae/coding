psum = [0] * 11
for i in range(1, 11):
    psum[i] += psum[i-1] + int(input())

chk = float('inf')
ans = 0 
for p in psum:
    if abs(100-p) <= chk:
        chk = abs(100-p)
        ans = max(ans, p)

print(ans)