#1
T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    gcd = []
    
    for j in range(1,min(a,b)+1):
        if a % j == 0 and b % j == 0:
            gcd.append(j)

    print(a * b // max(gcd))

#2
import math

T = int(input())
for i in range(T):
    a, b = map(int, input().split())

    print(a * b // math.gcd(a,b))
