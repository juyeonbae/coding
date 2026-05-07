import math 

def solution(a, b):
    x = math.gcd(a, b)
    a, b = a // x, b // x
    
    ans = set()
    i = 2
    
    while i*i <= b:
        while b % i == 0:
            ans.add(i)
            b //= i 
        i += 1
        
    if b > 1:
        ans.add(b)
    
    return 1 if ans <= {2, 5} else 2