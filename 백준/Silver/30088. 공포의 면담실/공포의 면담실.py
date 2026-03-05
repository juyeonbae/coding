import sys
input = sys.stdin.readline

n = int(input()) # 부서 수

arr = []
for _ in range(n):
    tmp = input().strip()
    x = sum(list(map(int, tmp[1:].split())))
    arr.append(x)

arr.sort()

p = [0] * (n+1)
for i in range(1, n+1):
    p[i] = p[i-1] + arr[i-1]

print(sum(p))