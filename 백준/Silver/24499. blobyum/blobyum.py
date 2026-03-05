import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = A + A  # 원형 처리
window = sum(B[:K])
ans = window

for i in range(K, K + N - 1):  
    window += B[i] - B[i-K]
    if window > ans:
        ans = window

print(ans)