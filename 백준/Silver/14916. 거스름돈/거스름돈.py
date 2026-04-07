import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
i = n//5

if n % 5 == 0:
    cnt = n // 5
else:  
    while i > -1:
        tmp = n - i * 5
        if tmp % 2 == 0:
            cnt = i + tmp // 2 
            break
        
        i -= 1
        
print(-1 if cnt == 0 else cnt)
