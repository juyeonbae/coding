import sys
input = sys.stdin.readline 

n = int(input())
lv = [int(input()) for _ in range(n)]

lv.sort()
x = int(n * 0.15 + 0.5)

avg = 0
for i in range(x, n-x):
    avg += lv[i] 

print(int(avg/(n-2*x)+0.5) if n > 0 else 0)