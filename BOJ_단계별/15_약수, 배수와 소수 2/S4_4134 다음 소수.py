#S4_4134 다음 소수.py

import sys
input = sys.stdin.readline

#isPrime
def isPrime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
    
#main
T = int(input())
for i in range(T):
    n = int(input())
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1
        
