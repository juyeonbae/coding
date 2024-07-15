import sys
input = sys.stdin.readline

n, m = map(int,input().split())

s = []
for i in range(n):
    s.append(input())
s = set(s)

cnt = 0
for i in range(m):
    chk = input()
    if chk in s:
        cnt += 1

print(cnt)
