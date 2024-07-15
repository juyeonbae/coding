import sys
input = sys.stdin.readline

#유클리드 호제법
import sys
input = sys.stdin.readline

def gcd(x,y):
    if y > x:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x

a, b = map(int,input().split())
gcd = gcd(a,b)
print(a*b//gcd)

#파이썬 라이브러리 내장 함수 사용 
import math
a,b = map(int,input().split())
print(math.lcm(a,b))

#반복문으로 풀이
a, b = map(int,input().split())
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(a * b // gcd)
