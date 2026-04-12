import sys
input = sys.stdin.readline

n = int(input())
t = [300, 60, 10]
answer = [0] * 3

for i in range(len(t)):
    answer[i] = n // t[i]
    n %= t[i] 

if n == 0: print(*answer)
else: print(-1)
    