import sys
input = sys.stdin.readline

n = int(input())
r = 1000 - n 

cnt = 0 
for i in [500, 100, 50, 10, 5, 1]:
    cnt += r // i 
    r = r % i 

print(cnt)
    