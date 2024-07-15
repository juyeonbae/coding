#factorial 함수 사용

import math
T = int(input())

for i in range(T):
    n, m = map(int,input().split())

    print(math.factorial(m)//((math.factorial(m-n) * math.factorial(n))))

#반복문 사용
T = int(input())
for i in range(T):
    n, m = map(int,input().split())
    x, y = 1, 1
    for j in range(m,m-n,-1):
        x *= j
    for k in range(1,n+1):
        y *= k

    print(x//y)

#combination 사용
from itertools import combinations as c
T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    x = len(list(c(range(1,m+1),n)))
    print(x)
